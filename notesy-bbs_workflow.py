from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import Mongodb, Cassandra
from diagrams.aws.compute import EC2
from diagrams.onprem.client import Users

with Diagram("NotesY-bbs_workflow", show=False):

    kafka = Kafka("stream")
    presentation = Users("Presentation")
    gateway = Server("API Gateway")

    presentation_bbs = Users("BBS Web")
    identityapi_bbs = EC2("BBS Identity API")
    identitydb_bbs = Cassandra("BBS Identity Db")

    identityapi_bbs - identitydb_bbs

    identityapi_bbs >> presentation_bbs
    identityapi_bbs << presentation_bbs


    with Cluster("Identity Service"):
        identitydb = Mongodb("Identity Db")
        identityapi = EC2("Identity API")
        gateway >> identityapi
        identityapi >> gateway
        identityapi - identitydb

    identityapi_bbs - identityapi

    with Cluster("Notes Service"):
        notesydb = Redis("Notes Db")
        notesyapi = EC2("Notesy API")
        gateway >> notesyapi
        notesyapi >> gateway
        notesyapi - notesydb
    
    presentation - gateway
    notesydb - kafka
    identitydb - kafka