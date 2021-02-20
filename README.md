# Tiger_Enterprise

**Ansible**

This folder contains 5 different yml files all of them have Ansible playbook code performing some kind of task.
Ex.

Ansible-hostname.yml - changes the hostname of ec2 instance

kubernetes-worker - Creates two new instance for worker nodes
                    Installs every required software for kubernetes
                    Configures kubernetes on the instances
                    Add both the worker nodes to a kubernestes cluster
                    

**API**

This folder contain two files, one is a Dockerfile which is used to create a docker and then the webapi.py file is compiled on the docker to get access of it
from the main instance.

**Bash**

This folder constains two bash scripts which are used to examine some log files
Both scripts prints the log files in a certain way which is easier to examine.


