from typing import Union
from schemas import UserRequest
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World."}



@app.post("/user")
def create_user(user:UserRequest):
    return {"message":"user created", "user":user}

# @app.get("/users/{user_name}") # path parameter
# def read_root(user_name:str = "admin"):
#     return {"Hello": user_name}


# @app.get("/admin") # Query parameter
# def read_root(name:str):
#     return {"Hello": name}