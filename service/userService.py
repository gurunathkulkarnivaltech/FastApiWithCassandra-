from model import *
from db import *
from cassandra.query import SimpleStatement
# Cassandra connection setup


def createUserService(user):
    session = connectDb("poc_database")
    try:
        # existingUserEmail = UserModel.get_user_by_email(email_id=user.email_id);
        # print(existingUserEmail.all())
        person = UserModel.create(name=user.name, age=user.age, gender=user.gender,
                                  email_id=user.email_id, password=user.password, mobileNo=user.mobileNo)

        return {"status": True, "data": person, "message": "SuccessFully created user"}
    except LookupError:
        print(LookupError)
        return {"status": False, "data": [], "message": "Error in inserting"}

def readDataService(page, page_size):
    try:
        session = connectDb("poc_database")
        offset = (page - 1) * page_size
        query = "SELECT * FROM user_model;"
        statement = SimpleStatement(query, fetch_size=10)
        results = session.execute(statement)
        # save page state
        page_state = results.paging_state
        print(page_state)
        for data in results:
            print(data.id)
            # process_data_here(data)
        # print(array)
    except LookupError:
        print(LookupError)
        return {"status": False, "data": [], "message": "Error in inserting"}