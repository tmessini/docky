from docker import Client
import localstore

def validate_containers(cluster_name):
    # Connection to Docker Daemon
    c = Client(base_url="unix://var/run/docker.sock")
    container_list = localstore.load_object(cluster_name + ".pkl")
    # Initialization
    checker = True
    if container_list is not None:
        # Checking all containers status
        for container in container_list:
            checker = checker * c.inspect_container(container).get("State").get("Running")
        if checker:
            print("Validation Success: All cluster [%s] nodes are up"%cluster_name)
        else:
            print("Validation Failure: Not all cluster [%s] nodes are up" %cluster_name)
    else:
        print("Cluster [%s] is not running"%cluster_name)


def stats(cluster_name, stats_type):
    # Connection to Docker Daemon
    c = Client(base_url="unix://var/run/docker.sock")
    container_list = localstore.load_object(cluster_name + ".pkl")
    containers = c.containers()
    if container_list is not None:
        # Checking all containers stats
        for container in container_list:
            containerid = c.inspect_container(container).get("Id")
            containerName = c.inspect_container(container).get("Name")
            print("Container Name:" + str(containerName) +  " Container Id:" + str(containerid) )
            # Get snapshot of statistics. Stats can be taken in stream format also.
            stats_obj = c.stats(containerid, False, False)
            if stats_type == "io":
                print(stats_obj.get("blkio_stats"))
            if stats_type == "precpu":
                print(stats_obj.get("precpu_stats"))
            if stats_type == "read":
                print(stats_obj.get("read"))
            if stats_type == "memory":
                print(stats_obj.get("memory_stats"))
            if stats_type == "pid":
                print(stats_obj.get("pids_stats"))
            if stats_type == "network":
                print(stats_obj.get("networks"))
            if stats_type == "cpu":
                print(stats_obj.get("cpu_stats"))
    else:
        print("Cluster [%s] is not running" % cluster_name)








