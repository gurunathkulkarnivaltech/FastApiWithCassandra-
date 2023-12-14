from pydantic import BaseModel, Field
from common import *
import re

class UserSchema(BaseModel):
    name: str
    age: int
    gender: str
    email_id: str
    password: str
    mobileNo: int
    
def ValidateUserSchema(user):
    obj = []
    if(user.name == ""):
        obj.append({"message": USER_SCHEMA_STRINGS["NAME_EMPTY"], "feild": "Name", "status": False})
    elif (user.age == ""):
        obj.append({"message": USER_SCHEMA_STRINGS["AGE_EMPTY"], "feild": "Age", "status": False})
    elif (user.gender == ""):
        obj.append({"message": USER_SCHEMA_STRINGS["GENDER_EMPTY"], "feild": "Gender", "status": False})
    elif (user.email_id == ""):
        obj.append({"message": USER_SCHEMA_STRINGS["EMAIL_EMPTY"], "feild": "Email_id", "status": False})
    elif (user.password == ""):
        obj.append({"message": USER_SCHEMA_STRINGS["PASSWORD_EMPTY"], "feild": "Password", "status": False})
    elif (user.mobileNo == ""):
        obj.append({"message": USER_SCHEMA_STRINGS["MOBILE_EMPTY"], "feild": "Mobile", "status": False})
    elif (len(str(user.mobileNo)) < 10):
        obj.append({"message": USER_SCHEMA_STRINGS["MOBILE_NOT_VALID"], "feild": "Mobile", "status": False})
    elif (user.email_id != ""):
        if (re.match(EMAIL_REGEX, user.email_id) == False):
            obj.append({"message": USER_SCHEMA_STRINGS["EMAIL_NOT_VALID"], "feild": "email_id", "status": False})
    elif(len(user.password) < 8):
        obj.append({"message": USER_SCHEMA_STRINGS["PASSWORD_NOT_VALID"], "feild": "password", "status": False})
    
    if (len(obj)):
        return { "status": False, "data": obj }
    else:    
        return { "status": True, "data": obj }
            
        