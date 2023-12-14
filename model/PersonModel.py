from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from uuid import uuid4


# Define Cassandra model using cqlengine
class PersonModel(Model):
    id = columns.UUID(primary_key=True, default=uuid4)
    name = columns.Text()
    age = columns.Integer()