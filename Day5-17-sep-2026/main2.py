from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Annotated,Literal
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserData(BaseModel):
    name: str
    gender:Annotated[Literal["male","female"],Field(...,description="Enter gender",examples=["male","female"])]
    dob: str
    parentage: str
    phonenumder:Annotated[int,Field(...,description="Enter a 10 digit phone number")] 
def loaddata():
    with open("data.json","r") as f:
        data=json.load(f)
        return data
def savedata(data):
    with open("data.json","w") as f:
        json.dump(data,f)


@app.post("/submit")
def submit_data(data: UserData):

    # Read existing data
    users=loaddata()

    # Add new data
    users.append(data.model_dump())

    # Save data
    savedata(users)
    return JSONResponse(status_code=200,content="user added sucessfully")
@app.get("/view/{name}")
def view_data(name:str):
    data=loaddata()
    for i in data:
        if i["name"] ==name:
            return i
    raise HTTPException(status_code=404,detail="User not found in the database")
@app.delete("/remove/{name}")
def remove_patient(name:str):
    data=loaddata()
    for i in data:
        if i["name"]==name:
            data.remove(i)
            savedata(data)
            return JSONResponse(status_code=201,content="User removed Sucessfully")
    raise HTTPException(status_code=404,detail="User not found")

