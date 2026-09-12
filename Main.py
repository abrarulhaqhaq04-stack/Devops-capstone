from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
from typing import Optional
import uuid

app = FastAPI(title="Todo API")

Instrumentator().instrument(app).expose(app)

# In-memory storage: {todo_id: {"id": ..., "title": ..., "done": ...}}
todos = {}


class TodoCreate(BaseModel):
    title: str
    done: bool = False


class Todo(TodoCreate):
    id: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    todo_id = str(uuid.uuid4())
    new_todo = Todo(id=todo_id, title=todo.title, done=todo.done)
    todos[todo_id] = new_todo
    return new_todo


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.get("/todos")
def list_todos():
    return list(todos.values())


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: str, todo: TodoCreate):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated_todo = Todo(id=todo_id, title=todo.title, done=todo.done)
    todos[todo_id] = updated_todo
    return updated_todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return {"detail": "Todo deleted"}
