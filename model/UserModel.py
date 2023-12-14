import datetime
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from uuid import uuid4

# Define Cassandra model using cqlengine
class UserModel(Model):
    id = columns.UUID(primary_key=True, default=uuid4)
    name = columns.Text()
    age = columns.Integer()
    gender = columns.Text()
    email_id = columns.Text()
    password = columns.Text()
    mobileNo = columns.BigInt()
    isActiveUser = columns.Boolean(default=True)
    
    def get_user_by_email(email_id):
        return UserModel.objects(email_id=email_id)
        
# UserModel.create_index("name")
# UserModel.create_index("email_id")