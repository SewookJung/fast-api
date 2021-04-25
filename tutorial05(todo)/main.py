from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


class Todo(BaseModel):
    name: str
    date: str
    desc: str


app = FastAPI(title="Todo app")


# C R U D

store_todo = []


@app.get("/")
def home():
    return {"Hello": "World"}


@app.post("/todo/")
def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo


@app.get("/todo/", response_model=List[Todo])
def get_all_todos():
    return store_todo


@app.get("/todo/{id}")
def get_todo(id: int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todo/{id}")
def update_todo(id: int, todo: Todo):
    try:
        store_todo[id] = todo
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todo/{id}")
def delete_todo(id: int):
    try:
        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404, detail="Todo not found")
