from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ---------------- DATABASE ----------------

DATABASE_URL = "postgresql://postgres:avisdb@localhost:5433/SQLalchemy_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# ---------------- SQLAlchemy Model ----------------

class TaskDB(Base):
    __tablename__ = "tasks"

    task_no = Column(Integer, primary_key=True, index=True)
    task_name = Column(String)

# Create table
Base.metadata.create_all(bind=engine)

# ---------------- Pydantic Model ----------------

class Task(BaseModel):
    task_no: int
    task_name: str

    class Config:
        from_attributes = True

# ---------------- FastAPI ----------------

app = FastAPI()

# ---------------- CREATE ----------------

@app.post("/tasks")
def create_task(task: Task):

    db = SessionLocal()

    existing = db.query(TaskDB).filter(TaskDB.task_no == task.task_no).first()

    if existing:
        db.close()
        raise HTTPException(status_code=400, detail="Task already exists")

    new_task = TaskDB(
        task_no=task.task_no,
        task_name=task.task_name
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()

    return new_task

# ---------------- GET ALL ----------------

@app.get("/tasks")
def get_tasks():

    db = SessionLocal()

    tasks = db.query(TaskDB).all()

    db.close()

    return tasks

# ---------------- GET ONE ----------------

@app.get("/tasks/{task_no}")
def get_task(task_no: int):

    db = SessionLocal()

    task = db.query(TaskDB).filter(TaskDB.task_no == task_no).first()

    db.close()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

# ---------------- UPDATE ----------------

@app.put("/tasks/{task_no}")
def update_task(task_no: int, task: Task):

    db = SessionLocal()

    existing = db.query(TaskDB).filter(TaskDB.task_no == task_no).first()

    if not existing:
        db.close()
        raise HTTPException(status_code=404, detail="Task not found")

    existing.task_name = task.task_name
    existing.task_no = task.task_no

    db.commit()
    db.refresh(existing)

    db.close()

    return existing

# ---------------- DELETE ----------------

@app.delete("/tasks/{task_no}")
def delete_task(task_no: int):

    db = SessionLocal()

    task = db.query(TaskDB).filter(TaskDB.task_no == task_no).first()

    if not task:
        db.close()
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    db.close()

    return {"message": "Task deleted"}