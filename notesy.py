from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import Mongodb
from diagrams.aws.compute import EC2
from diagrams.onprem.client import Users

with Diagram("NotesY Service", show=False):

    kafka = Kafka("stream")
    presentation = Users("Presentation")

    with Cluster("API Gateway"):
        gateway = [
            Server("API Gateway")]

    with Cluster("Identity Service"):
        identitydb = Mongodb("Identity Db")
        identityapi = EC2("Identity API")
        gateway >> identityapi
        identityapi >> gateway
        identityapi - identitydb

    with Cluster("Notes Service"):
        notesydb = Redis("Notes Db")
        notesyapi = EC2("Notesy API")
        gateway >> notesyapi
        notesyapi >> gateway
        notesyapi - notesydb
    
    presentation - gateway
    notesydb - kafka
    identitydb - kafka