# requires `pip install diagrams` 
# graphviz library is a prerequisite and will be automatically installed
# requires installatation of graphviz on PC from here: https://graphviz.org/download/
# add C:\Program Files\Graphviz\bin added to the %PATH%

# https://diagrams.mingrammer.com/
# https://bluelight.co/blog/diagrams-as-code
# Unified Modeling Language (UML)


from diagrams import Cluster, Diagram, Node, Edge
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.onprem.database import MongoDB
from diagrams.gcp.storage import GCS
from diagrams.gcp.database import SQL, BigTable
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
from diagrams.gcp.compute import AppEngine, Functions
from diagrams.gcp.iot import IotCore
from diagrams.gcp.storage import GCS



with Diagram('My Diagram'):
    BigQuery('Data Warehouse')

with Diagram('My Diagram'):
    Node('This is a custom node')    

with Diagram('My Diagram', direction='TB'):
    gcs = GCS('Google Cloud Storage')
    with Cluster('Databases'):
        cloud_sql = SQL('Cloud SQL')
        mongodb = MongoDB('MongoDB')


with Diagram("Simple Web Service with DB Cluster", show=False):
    dns = Route53("dns")
    web = ECS("service")

    with Cluster("DB Cluster"):
        db_primary = RDS("primary")
        db_primary - [RDS("replica1"),
                     RDS("replica2")]

    dns >> web >> db_primary


with Diagram('My Diagram', direction='TB'):
    n1 = Node('n1')
    n2 = Node('n2')
    n3 = Node('n3')
    n4 = Node('n4')
    n5 = Node('n5')
    n6 = Node('n6')   
    
    n1 >> n2
    n3 - n4
    n5 >> Edge(label='This is a label', color='red') >> n6    


with Diagram("Message Collecting", show=True):
    pubsub = PubSub("pubsub")

    with Cluster("Source of Data"):
        [IotCore("core1"), IotCore("core2"), IotCore("core3")] >> pubsub

    with Cluster("Targets"):
        with Cluster("Data Flow"):
            flow = Dataflow("data flow")

    with Cluster("Data Lake"):
        flow >> [BigQuery("bq"),
                    GCS("storage")]

    with Cluster("Event Driven"):
        with Cluster("Processing"):
            flow >> AppEngine("engine") >> BigTable("bigtable")

    with Cluster("Serverless"):
        flow >> Functions("func") >> AppEngine("appengine")
    
    pubsub >> flow    