# 4. Linking Nodes Diagram

from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.onprem.database import PostgreSQL # Would typically use RDS from aws.database
from diagrams.onprem.inmemory import Redis # Would typically use ElastiCache from aws.database

def linking_nodes_diagram():
    with Diagram("Simple Website Diagram", direction='LR') as diag4: # It's LR by default, but you have a few options with the orientation
        dns = Route53("DNS")
        load_balancer = ELB("Load Balancer")
        database = PostgreSQL("User Database")
        cache = Redis("Cache")
        with Cluster("Webserver Cluster"):
            svc_group = [EC2("Webserver 1"),
                        EC2("Webserver 2"),
                        EC2("Webserver 3")]
        dns >> load_balancer >> svc_group
        svc_group >> cache
        svc_group >> database
    print(diag4) # This will illustrate the diagram if you are using a Google Colab or Jypiter notebook.

linking_nodes_diagram()
