from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# example data 
tasks = [
    {"id": 1, "title": "Task 1", "description": "This is task 1"},
    {"id": 2, "title": "Task 2", "description": "This is task 2"},
    # {"id": 3, "title": "Task 3", "description": "This is task 3"},
    # {"id": 4, "title": "Task 4", "description": "This is task 4"},
    # {"id": 5, "title": "Task 5", "description": "This is task 5"},
    # {"id": 6, "title": "Task 6", "description": "This is task 6"},
]

class Task(BaseModel):
    title: str
    description: str

@app.get("/")
def read_root():
    return {"message":"Hakuna matata!"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.get("/tasks/{id}")
def get_tasks(id: int):
    for task in tasks:
        if task["id"] == id:
            return {"task": task}
    return {"task": None}

@app.post("/tasks")
def create_task(task: Task):
    new_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {"id": new_id, "title": task.title, "description": task.description}
    tasks.append(new_task)
    return {"task": new_task}

@app.put("/tasks/{id}")
def update_task(id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            return {"task": task}
    return {"error": "Task not found"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for i, task in enumerate(tasks):
        if task["id"] == id:
            deleted_task = tasks.pop(i)
            return {"deleted": deleted_task}
    return {"error": "Task not found"}




