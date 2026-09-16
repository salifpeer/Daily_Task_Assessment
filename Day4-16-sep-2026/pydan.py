from typing import List, Dict,Optional,Annotated
from pydantic import BaseModel, EmailStr,AnyUrl,field_validator,computed_field
class patient(BaseModel):
    name:str
    age:int
    weight:float
    height:float
    married:bool
    contact:Dict[str,str]
    allergies:List[str]
    email:str
    @computed_field
    @property
    def bmi(self)->str:
        bmi=self.weight/(self.height*self.height)
        return bmi
    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid=["icici.com","gmail.com","cyberx.com"]
        domain=value.split("@")[-1]
        if domain not in valid:
            raise ValueError("Email not found")
        return value

mydic={"name":"salif","age":25,"weight":65,"height":10,"married":False,"contact":{"phone":"8899778866"},"allergies":["jj","hhk"],"email":"salif@gmail.com"}
pat=patient(**mydic)
print(pat.bmi)
        

