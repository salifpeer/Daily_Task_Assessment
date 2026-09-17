from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
import json
from typing import Literal,Annotated,Optional
from pydantic import BaseModel,computed_field,Field

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
class patient(BaseModel):
    pid:Annotated[str,Field(...,description="id of the patient",examples=["p001"])]
    name:Annotated[str,Field(...,description="name of the patient",examples=["salif"])]
    height:Annotated[float,Field(...,description="height of the patient",gt=0)]
    weight:Annotated[float,Field(...,description="weight of the patient",gt=0)]
    gender:Annotated[Literal["male","female"],Field(...,description="name of the patient")]
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height*self.height),2)
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18:
            return "Underweight"
        elif self.bmi<25:
            return "Normal"
        elif self.bmi<30:
            return "Overweight"
        else:
            return "Obese"

class updated_patient(BaseModel):
    name:Annotated[Optional[str],Field(default=None,description="name of the patient",examples=["salif"])]
    height:Annotated[Optional[float],Field(default=None,description="height of the patient",gt=0)]
    weight:Annotated[Optional[float],Field(description="weight of the patient",default=None,gt=0)]
    gender:Annotated[Optional[Literal["male","female"]],Field(description="name of the patient",default=None)]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def save_data(data):
    with open("user.json","w") as f:
        json.dump(data,f)

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
#adding new patients to database
@app.post("/create")
def create_patient(Patient:patient):
    data=loaddata()
    if Patient.pid in data:
        raise HTTPException(status_code=400,detail="Id already exists")
    data[Patient.pid]=Patient.model_dump(exclude=["pid"])
    save_data(data)
    return JSONResponse(status_code=201,content="patient created sucessfully")
#modifying the existing data
@app.put("/edit_patient/{pid}")
def edit(pid:str,Patient:updated_patient):
    data=loaddata()
    if pid not in data:
        raise HTTPException(status_code=401,detail="Patient not available")
    existing_data=data[pid]
    updated_data=Patient.model_dump(exclude_unset=True)
    for key,value in updated_data.items():
        existing_data[key]=value
    existing_data["pid"]=pid
    updated_model=patient(**existing_data)
    updated_data=updated_model.model_dump(exclude=["pid"])
    data[pid]=updated_data
    save_data(data)
    return JSONResponse(status_code=202,content="patient details updated sucess fully")
@app.delete("/Remove patient/{pid}")
def remove_patient(pid:str):
    data=loaddata()
    if pid not in data:
        print('inside if')
        raise HTTPException(status_code=404,detail="patient not found")
    del data[pid]
    save_data(data)
    return JSONResponse(status_code=200,content="patient removed sucessfully")


