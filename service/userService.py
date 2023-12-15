from model import *
from db import *
from cassandra.query import SimpleStatement
# Cassandra connection setup


def createUserService(user):
    session = connectDb("poc_database")
    try:
        person = UserModel.create(name=user.name, age=user.age, gender=user.gender,
                                  email_id=user.email_id, password=user.password, mobileNo=user.mobileNo)

        return {"status": True, "data": person, "message": "SuccessFully created user"}
    except LookupError:
        print(LookupError)
        return {"status": False, "data": [], "message": "Error in inserting"}


def readDataService(page, page_size, token=''):
    try:
        session = connectDb("poc_database")
        if token:
            query = "SELECT name, age, token(id) as rowId, gender, email_id   FROM user_model where token(id) > {} limit {};".format(
                token, page_size)
        else:
            query = "SELECT name, age, token(id) as rowId, gender, email_id FROM user_model limit {};".format(
                page_size)
        statement = SimpleStatement(query, fetch_size=10)
        results = session.execute(statement)
        responseObj = []
        for data in results:
            # print('Name: {} , Row ID: {}'.format(data.name, data.rowid))
            responseObj.append({"name": data.name, "rowId": data.rowid, "age": data.age,
                               "gender": data.gender, "email_id": data.email_id})
        print(responseObj)
        return responseObj
    except LookupError:
        print(LookupError)
        return {"status": False, "data": [], "message": "Error in inserting"}
