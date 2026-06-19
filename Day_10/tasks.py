from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Task(BaseModel):
    task_name: str
    task_no: int



app = FastAPI()

tasks =[
    Task(task_name="project", task_no=1),
    Task(task_name="git push", task_no=2)
]

@app.post("/tasks")
def add_task(task: Task):
    if task not in tasks:
        tasks.append(task)
        return task
@app.get("/tasks")
def all_task():
    return tasks
@app.get("/tasks/{task_no}")
def specific_task(task_no: int):
    for task in tasks:
        if task.task_no == task_no:
            return task
    raise HTTPException(status_code=404,detail="Task not found")
@app.put("/tasks")
def update_tasks(task_no: int,task: Task):
    for i in range(len(tasks)):
        if tasks[i].task_no == task_no:
            tasks[i]==task
    raise HTTPException(status_code=404,detail="Task not found")
@app.delete("/tasks")
def task_remove(task_no: int):
    for task in tasks:
        if task.task_no == task_no:
            tasks.remove(task)
            return "task removed"
    raise HTTPException(status_code=404,detail="Task not found")
