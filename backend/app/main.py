from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List
from .database import Base, engine, SessionLocal
from .models import Task
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",  # your frontend dev server
    # you can add other origins if needed
]


# Create tables if they don't exist
Base.metadata.create_all(bind=engine) 

# Dependency to give each request a DB session 
# This means that whenever we send a request, we open a session with the db
#  and after the HTTP request interaction, we close this session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schemas
class TaskCreate(BaseModel):
    title: str
    description: str

class TaskOut(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# THINGS THAT WERE JUST FOR PRACTICE, BUT IM STILL KEEPING THEM HERE SO THAT I REMEMBER WHERE I CAME FROM
# example data 
# tasks = [
#     {"id": 1, "title": "Task 1", "description": "This is task 1"},
#     {"id": 2, "title": "Task 2", "description": "This is task 2"},
#     # {"id": 3, "title": "Task 3", "description": "This is task 3"},
#     # {"id": 4, "title": "Task 4", "description": "This is task 4"},
#     # {"id": 5, "title": "Task 5", "description": "This is task 5"},
#     # {"id": 6, "title": "Task 6", "description": "This is task 6"},
# ]

# class Task(BaseModel):
#     title: str
#     description: str

@app.get("/")
def read_root():
    return {"message":"Hakuna matata!"}


# gets all tasks
@app.get("/tasks", response_model=List[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

# returns one single specific task
@app.get("/tasks/{id}", response_model=TaskOut)
def get_tasks(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task:
        return task
    return {"error": "Task not found"}


# adds one task to the tasks table
@app.post("/tasks", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# edits a task
@app.put("/tasks/{id}", response_model=TaskOut)
def update_task(id: int, updated_task: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task:
        task.title = updated_task.title
        task.description = updated_task.description
        db.commit()
        db.refresh(task)
        return task
    return {"error": "Task not found"}

# deletes a task
@app.delete("/tasks/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"deleted": {"id": task.id, "title": task.title, "description": task.description}}
    return {"error": "Task not found"}
