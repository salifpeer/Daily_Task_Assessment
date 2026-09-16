from fastapi import FastAPI,Path,HTTPException,Query
import json

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def loaddata():
    with open("user.json","r") as f:
        data=json.load(f)
        print(data)
    return data
#displaying a message on screen
@app.get("/")
def user():
    return {"message":"Welcome"}
#getting all the patient details
@app.get("/view")
def View(pid:str=Query("none",detail="Enter a specific id")):
    data=loaddata()
    if pid=="none":
        return data
    return data[pid] 
#getting a particular patent detalis
@app.get("/view/{patient_id}")
def view_patient(patient_id:str=Path(...,description="Enter the id of any patient", example="p001")):
    data=loaddata()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=400,detail="Id not available")
