from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import Cassandra, Mongodb
from diagrams.aws.compute import EC2
from diagrams.onprem.client import Users

with Diagram("BigBrain Solutions Web", show=False):

    presentation = Users("Presentation")
    identityapi = EC2("BBS Identity API")
    identitydb = Cassandra("BBS Identity Db")

    presentation >> identityapi
    presentation << identityapi

    identityapi - identitydb