from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    task_no = Column(Integer, primary_key=True, index=True)
    task_name = Column(String)
    status = Column(String)


class Task1(BaseModel):
    task_no: int
    task_name: str
    status: str
    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db                    # concept?
    finally:
        db.close()

app = FastAPI()

# tasks =[
#     Task(task_name="project", task_no=1),
#     Task(task_name="git push", task_no=2)
# ]

@app.post("/tasks")
def add_task(task: Task1, db: Session = Depends(get_db)):
    exist_task = db.query(Task).filter(Task.task_no == task.task_no).first()
    if exist_task:
        # db.close()
        raise HTTPException(status_code=409,detail="Task exist already")
    new_task = Task(task_no=task.task_no,task_name=task.task_name,status=task.status)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    # db.close()
    return new_task

    
@app.get("/tasks")
def all_task(db: Session = Depends(get_db)):
    # db = SessionLocal()
    tasks = db.query(Task).all()
    # db.close()
    return tasks

@app.get("/tasks/{task_no}")
def specific_task(task_no: int,db: Session = Depends(get_db)):
    # db = SessionLocal()
    task = db.query(Task).filter(Task.task_no == task_no).first()
    if not task:
        # db.close()
        raise HTTPException(status_code=404, detail="Task not found")
    # db.close()
    return task
    

@app.put("/tasks/{task_no}")
def update_tasks(task_no: int,task: Task1, db: Session = Depends(get_db)):
    # db = SessionLocal()
    task_exist = db.query(Task).filter(Task.task_no == task_no).first()
    if task_exist:
        task_exist.task_no = task.task_no
        task_exist.task_name = task.task_name
        task_exist.status = task.status
        db.commit()
        db.refresh(task_exist)
        # db.close()
        return task_exist
    else:
        # db.close()
        raise HTTPException(status_code=404,detail="Task not found")

@app.delete("/tasks/{task_no}")
def task_remove(task_no: int, db: Session = Depends(get_db)):
    # db = SessionLocal()
    task = db.query(Task).filter(Task.task_no == task_no).first()
    if task:
        db.delete(task)
        db.commit()
        # db.close()
        return {"message":"Task deleted"}
    else:
        # db.close()
        raise HTTPException(status_code=404,detail="Task not found")