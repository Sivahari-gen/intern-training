from fastapi import FastAPI
from pydantic import BaseModel

class intern(BaseModel):
    id: int
    name: str

app = FastAPI()

interns = []

@app.get("/interns")
def view():
    return interns

@app.post("/interns")
def intern_add(add: intern):
    interns.append(add)
    return interns

@app.put("/interns/{id}")
def intern_update(id: int,update: intern):
    for i in range(len(interns)):
        if interns[i].id==id:
            interns[i]=update

    return interns

@app.delete("/interns/{id}")
def intern_del(id: int):
    for i in range(len(interns)):
        if interns[i].id == id:
            interns.pop(i)
            return interns