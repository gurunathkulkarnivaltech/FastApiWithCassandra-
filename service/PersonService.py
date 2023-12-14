from model import *
from db import *
# Cassandra connection setup

def createPerson(name, age):
    connectDb()
    person = PersonModel.create(name=name, age=age)
    return {"id": str(person.id), "name": person.name, "age": person.age}
    

def readPerson():
    connectDb()
    obj = PersonModel.all()
    data = []
    for p in obj:
        data.append(p);
    return data