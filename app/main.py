from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
from typing import Dict
import uuid

app = FastAPI(title="Todo API", description="Simple Todo API for DevOps capstone project")

# Expose /metrics for Prometheus scraping
Instrumentator().instrument(app).expose(app)

# In-memory store (swap for a real DB later if you want)
todos: Dict[str, dict] = {}


class Todo(BaseModel):
    title: str
    done: bool = False


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/todos")
def list_todos():
    return todos


@app.post("/todos")
def create_todo(todo: Todo):
    todo_id = str(uuid.uuid4())
    todos[todo_id] = todo.dict()
    return {"id": todo_id, **todo.dict()}


@app.get("/todos/{todo_id}")
def get_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]


@app.put("/todos/{todo_id}")
def update