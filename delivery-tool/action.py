import os
import sys
import connection

from docker import Client

import localstore


def show_containers():
    # Connection to Docker Daemon
    c = connection.get()
    # Showing containers
    containers = c.containers()
    for container in containers:
       print(container.get('Id'))


def start_cluster(cluster_name, size, image):
    c = connection.get()
    container_list = []
    # Simple iteration for starting containers
    for i in range(0, size):
        cname = "%s-node%s" % (cluster_name, i)
        try:
            container = c.create_container(image, name=cname, ports=[8080])
            container_list.append(container)
            c.start(container, publish_all_ports=True)
        except Exception as err:
            print("Unexpected error:", sys.exc_info()[0])
            print('Handling run-time error:', err)
    # Saving locally cluster nodes
    localstore.save_object(container_list, cluster_name + ".pkl")


def stop_cluster(cluster_name):
    # Connection to Docker Daemon
    c = connection.get()
    # Loading containers from localstore
    container_list = localstore.load_object(cluster_name + ".pkl")
    if container_list is not None:
        for container in container_list:
            # We need to stop the containers
            try:
                print("Stopping container: " + str(container))
                c.stop(container, 10)
                c.remove_container(container)
            except:
                print("Unexpected error:", sys.exc_info()[0])
        # Delete local store of cluster nodes
        os.remove(cluster_name+".pkl")
    else:
        print("Cluster [%s] is not running" % cluster_name)