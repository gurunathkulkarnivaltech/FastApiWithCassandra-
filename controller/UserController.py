from fastapi import APIRouter, Query
from model import *
from service import *
from Schema import *
from common import *


router = APIRouter()


@router.post("/user/", response_model=None)
async def create_User(user: UserSchema):
    # validation of Request Body
    schemaValid = ValidateUserSchema(user)
    if (schemaValid["status"] == True):
        createdUser = createUserService(user)
        if (createdUser["status"] == True):
            return sendResponse(API_SUCCESS_MESSAGE, createdUser,{} ,True, SUCCESS_STATUS_CODES["API_SUCCESS_STATUS_CODE"])
        else:
            return sendResponse(API_FAILED_MESSAGE, [],createdUser ,True, ERROR_STATUS_CODES["API_FAILED_STATUS_CODE"])
    else:
        return sendResponse(VALIDATION_FAILED_MESSAGE, [], schemaValid["data"], False, ERROR_STATUS_CODES["VALIDATION_ERROR_STATUS_CODE"])

DEFAULT_PAGE_SIZE = 10
@router.get("/user/", response_model=None)
async def getUser(page: int = Query(1, ge=1), page_size: int = Query(DEFAULT_PAGE_SIZE, le=100), token: int = Query('')):
    response = readDataService(page, page_size, token);
    return sendResponse(API_SUCCESS_MESSAGE, response,{} ,True, SUCCESS_STATUS_CODES["API_SUCCESS_STATUS_CODE"])