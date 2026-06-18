from fastapi import FastAPI
app = FastAPI()

interns = {}

@app.get("/interns")
def view():
    return interns

@app.post("/interns/{id}")
def intern_add(id: int,name: str):
    interns[id]={
        "name": name,
    }
    return interns[id]

@app.put("/interns/{id}")
def intern_update(id: int,name: str):
    interns[id]["name"]=name
    return interns[id]

@app.delete("/interns/{id}")
def intern_del(id: int,name: str):
    interns.pop(id)
    return {"notice":"intern delted"}