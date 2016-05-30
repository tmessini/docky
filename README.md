# delivery-tool
Tool for docker container management (e.g. deployments, monitoring)

# A.1 BUILDING THE CONTAINER
The container that is to form the java-webapp-cluster is a web application on Bootstrap (microservice)
In order to build it we need to have java, maven installed

mvn package docker:build

# A.2 RUNNING MANUALLY THE CONTAINER
After the container is built with name tmessinis/dockerized-service we can try to deploy it manually:

docker run -p 8080:8080 tmessinis/dockerized-service

docker ps

docker stop containerId

# B.1. DEPENDENCIES INSTALLATION FOR PYTHON TOOL (delivery tool)

sudo apt-get install python-pip

sudo pip install docker-py

# B.2. TOOL USE CASES:
Show help options of delivery tool

python main.py -h 

# B.2.1. Start a few instances of the Docker image in different containers.

python main.py -action start  -name java-webapp-cluster -size 10

# B.2.2. Stop a cluster of different Docker containers.

python main.py -action stop -name java-webapp-cluster

# B.2.3. Validate that the container images are running.

python main.py -monitor status -name java-webapp-cluster

# B.2.4. Monitor resource usage of each container (CPU, IO).

python main.py -monitor cpu -name java-webapp-cluster

python main.py -monitor io -name java-webapp-cluster

python main.py -monitor memory -name java-webapp-cluster

python main.py -monitor pid -name java-webapp-cluster

python main.py -monitor network -name java-webapp-cluster

python main.py -monitor precpu -name java-webapp-cluster

# B.2.5. Consolidate the log output of all the containers into a centralized log file.

python main.py -log java-cluster.txt -name java-webapp-cluster
