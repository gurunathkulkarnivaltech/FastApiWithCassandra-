from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from model import *
from cassandra.cluster import Cluster


# Cassandra connection setup
def SetupDb():
    connection.setup(['localhost'], "poc_database", protocol_version=4)
    sync_table(model=PersonModel)
    sync_table(model=UserModel)
    
def connectDb(my_keyspace):
    # connection with cassandra
    cluster = Cluster(["127.0.0.1"])
    session = cluster.connect()
    # setting keyspace
    session.set_keyspace(my_keyspace)
    return session
