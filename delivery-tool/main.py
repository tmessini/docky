import argparse
import action
import monitor
import log

# Parse the command line arguments
parser = argparse.ArgumentParser(description='Tool for basic management of docker containers')

# Cluster Configuration
parser.add_argument('-size', metavar="cluster_size", type=int, help='size of cluster')
parser.add_argument('-image', metavar="docker_image_location", type=str, default="tmessinis/dockerized-service",
                    help='image of dockerized application (e.g. tmessinis/dockerized-service)')
parser.add_argument('-name', metavar="cluster_image_name", type=str, default="service-cluster",
                    help='cluster name (e.g. service-cluster)')

# Lifecycle
parser.add_argument('-action', metavar="lifecycle_commands", type=str, help='lifecycle actions (e.g. start, stop)')

# Monitor
parser.add_argument('-monitor', metavar="container_variable", type=str, help='monitor the cluster (e.g. status, cpu, io)')

# Logs
parser.add_argument('-logs', metavar="path_to_logs", type=str, help='configure path consolidated logs')

# Parse Arguments
args = parser.parse_args()
print(args)

# Configuration
if args.name is not None:
    print("Cluster name is: " + str(args.name))

if args.size is not None:
    print("Cluster size is: " + str(args.size))

if args.image is not None:
    print("Cluster image is: " + str(args.image))

# Logs
if args.logs is not None:
    print("Setting path for logs: " + str(args.logs))
    log.consolidate_logs(args.name, args.logs)

# Lifecycle
if args.action == "start":
    print("Starting cluster with name [%s]  which is composed of [%s] nodes of docker image [%s]" % (
        str(args.name), str(args.size), str(args.image)))
    assert isinstance(args.image, object)
    action.start_cluster(args.name, args.size, args.image)

if args.action == "stop":
    print("Stopping cluster with name [%s]" % (str(args.name)))
    action.stop_cluster(args.name)

# Monitor
if args.monitor == "status":
    print("Checking containers status..")
    monitor.validate_containers(args.name)

if args.monitor == "cpu":
    print("Checking containers CPU...")
    monitor.stats(args.name, "cpu")

if args.monitor == "io":
    print("Checking containers IO...")
    monitor.stats(args.name, "io")

if args.monitor == "precpu":
    print("Checking containers PRECPU...")
    monitor.stats(args.name, "precpu")

if args.monitor == "read":
    print("Checking containers READ...")
    monitor.stats(args.name, "read")

if args.monitor == "memory":
    print("Checking containers MEMORY...")
    monitor.stats(args.name, "memory")

if args.monitor == "pid":
    print("Checking containers PID...")
    monitor.stats(args.name, "io")

if args.monitor == "network":
    print("Checking containers NETWORK...")
    monitor.stats(args.name, "network")





# USE CASES:
# 1. Start a few instances of the Docker image in different containers.
# python main.py -action start  -name cluster -size 10

# 2. Stop a cluster of different Docker containers.
# python main.py -action stop -name cluster

# 3. Validate that the container images are running.
# python main.py -monitor status -name cluster

# 4. Monitor resource usage of each container (CPU, IO).
# python main.py -monitor cpu -name cluster
# python main.py -monitor io -name cluster
# python main.py -monitor memory -name cluster
# python main.py -monitor pid -name cluster
# python main.py -monitor network -name cluster
# python main.py -monitor precpu -name cluster

# 4. Consolidate the log output of all the containers into a centralized log file.
# python main.py -log logfile.txt -name yolo-cluster
