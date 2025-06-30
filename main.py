from fastapi import FastAPI

import uvicorn
from pydantic import BaseModel, EmailStr
from items_views import router as items_router
from Users.views import router as users_router
app = FastAPI()
app.include_router(items_router, prefix="/items-views")
app.include_router(users_router)

@app.get("/")
def indexing():
    return{
        "message":"Walewildering",
    }

@app.post("/calc/add")
async def add(a:int, b:int):
    return {
        "a":a,
        "b":b,
        "result":a+b
    }

@app.get("/forcen/")
def forcen(name:str = "Pleb?"):
    name = name.strip().title()
    return{
        "message":f"Hey {name}",
    }







if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
