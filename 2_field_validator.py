from pydantic import BaseModel, Field, ValidationError, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    name:str
    email: EmailStr
    age:int 
    weight: float
    married: bool 
    allergies:List[str]
    contact_info: Dict[str, str]
#field_validator is used to validate the fields of the model, it is a class method that takes the value of the field as an argument and returns the validated value or raises a ValueError if the validation fails.
    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        valid_domain=["hdfc.com",'icici.com']
        domain_name=value.split('@')[-1]    
        if domain_name not in valid_domain:
            raise ValueError("Not a valid email")
        return value

    @field_validator("name")
    @classmethod
    def transform_name(cls, value: str) -> str:
        return value.title()

    @field_validator("age",mode='before')
    @classmethod
    def validate_age(cls, value: int) -> int:
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        return value
    
    @field_validator("weight",mode='after')
    @classmethod
    def validate_weight(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("Weight must be greater than 0")
        return value

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print("Patient data updated successfully.")

patient_info = {
    "name": "achal yadav",
    "email": "achallamba@hdfc.com",    
    "age": 30,  
    "weight": '70.5',# type conversion will be handled by Pydantic
    "married": True,
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {"phone": "123-456-7890", "address": "123 Main St"}
}

patient= Patient(**patient_info)  # Create an instance of the Patient model

update_patient_data(patient)  # Update the patient data