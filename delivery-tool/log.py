from threading import Thread
from docker import Client
import localstore


def threaded_function(logs_steam, logs, container_name):
    with open(logs, 'ab') as f:
        for log_line in logs_steam:
            f.write("[%s]"%container_name+log_line)

def consolidate_logs(cluster_name, logs):
    # Connection to Docker Daemon
    c = Client(base_url="unix://var/run/docker.sock")
    container_list = localstore.load_object(cluster_name + ".pkl")
    if container_list is not None:
        # Checking all containers logs
        for container in container_list:
            logs_stream = c.logs(container, stream=True, stdout=True, stderr=True)
            container_name = c.inspect_container(container).get("Name")
            print("Staring logging for: ", container_name)
            thread= Thread(target=threaded_function, args=(logs_stream,logs, container_name))
            thread.setDaemon(True)
            thread.start()
    else:
        print("Cluster [%s] is not running" % cluster_name)
