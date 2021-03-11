## Architectural Diagrams with Python
##  https://towardsdatascience.com/create-beautiful-architecture-diagrams-with-python-7792a1485f97
## https://colab.research.google.com/drive/10Nq0KmjbgvAzcaLiqQPwMeDVdkHBCy6y

def simple_diagram():
    from diagrams import Diagram

    with Diagram("Simple Website Diagram") as diag:
        pass
    print(diag) # This will illustrate the diagram if you are using a Google Colab or Jypiter notebook.

def nodes_diagram():
    from diagrams import Diagram, Cluster
    from diagrams.aws.compute import EC2
    from diagrams.aws.network import ELB
    from diagrams.aws.network import Route53
    from diagrams.onprem.database import PostgreSQL # Would typically use RDS from aws.database
    from diagrams.onprem.inmemory import Redis # Would typically use ElastiCache from aws.database

    with Diagram("Simple Website Diagram") as diag2:
        dns = Route53("dns")
        load_balancer = ELB("Load Balancer")
        database = PostgreSQL("User Database")
        cache = Redis("Cache")
        svc_group = [EC2("Webserver 1"),
                    EC2("Webserver 2"),
                    EC2("Webserver 3")]
    print(diag2) # This will illustrate the diagram if you are using a Google Colab or Jypiter notebook.


def group_nodes_diagram():
    from diagrams import Diagram, Cluster
    from diagrams.aws.compute import EC2
    from diagrams.aws.network import ELB
    from diagrams.aws.network import Route53
    from diagrams.onprem.database import PostgreSQL # Would typically use RDS from aws.database
    from diagrams.onprem.inmemory import Redis # Would typically use ElastiCache from aws.database

    with Diagram("Simple Website Diagram") as diag3:
        dns = Route53("dns")
        load_balancer = ELB("Load Balancer")
        database = PostgreSQL("User Database")
        cache = Redis("Cache")
        with Cluster("Webserver Cluster"):
            svc_group = [EC2("Webserver 1"),
                        EC2("Webserver 2"),
                        EC2("Webserver 3")]
    print(diag3) # This will illustrate the diagram if you are using a Google Colab or Jypiter notebook.


def linking_nodes_diagram():
    from diagrams import Diagram, Cluster
    from diagrams.aws.compute import EC2
    from diagrams.aws.network import ELB
    from diagrams.aws.network import Route53
    from diagrams.onprem.database import PostgreSQL # Would typically use RDS from aws.database
    from diagrams.onprem.inmemory import Redis # Would typically use ElastiCache from aws.database

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


if __name__ == "__main__":
    """
        $ sudo apt install graphviz
        $ pip3 install diagrams
        ## Uncomment the function for printing diagram flow
    """

    # 1. Basic diagram
    # simple_diagram()

    # 2. Adding the Nodes
    # nodes_diagram()

    # 3. Grouping the Nodes
    # group_nodes_diagram()

    # 4. Linking Nodes
    linking_nodes_diagram()
