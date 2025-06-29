from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, EmailStr
app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr
@app.get("/")
def indexing():
    return{
        "message":"Walewildering",
    }

@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message":"success",
        "email":user.email
    }
@app.post("/calc/add")
async def add(a:int, b:int):
    return {
        "a":a,
        "b":b,
        "result":a+b
    }
@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3"
    ]
@app.get("/forcen/")
def forcen(name:str = "Pleb?"):
    name = name.strip().title()
    return{
        "message":f"Hey {name}",
    }

@app.get("/items/latest/")
def get_latest_item():
    return{
        "item":{"id":"0", "name":"latest"}
    }
@app.get("/items/{item_id}/")
def get_item_by_id(item_id:int):
    return{
        "item":{
            "id":item_id,
        }
    }





if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
