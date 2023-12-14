from fastapi import FastAPI, HTTPException
from uuid import uuid4
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from controller import UserController, PersonController
from db import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SetupDb()
app.include_router(UserController.router)
app.include_router(PersonController.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
