from docker import Client


def get():
   return Client(base_url='unix://var/run/docker.sock')