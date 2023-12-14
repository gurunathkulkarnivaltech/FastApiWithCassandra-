from fastapi import APIRouter, HTTPException
from model import *
from service import *

router = APIRouter()


@router.post("/people/", response_model=None)
async def create_person(name: str, age: int):
    response = createPerson(name=name, age=age)
    return response


@router.get("/people/", response_model=None)
async def read_person():
        response = readPerson()
        return response
