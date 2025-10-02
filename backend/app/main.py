from fastapi import FastAPI

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



