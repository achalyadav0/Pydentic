from pydantic import BaseModel, Field, ValidationError
from typing import List, Dict, Optional, Annotated

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class Patient(BaseModel):
    name: str
    email: str  
    age: int
    weight: float
    married: bool = False
    address:Address

address_info = {
    "street": "123 Main St",
    "city": "Springfield",
    "state": "IL",
    "zip_code": "62701"
}
address = Address(**address_info)
patient_info = {
    "name": "achal yadav",
    "email": "achalyadav@gmail.com",
    "age": 34,      
    "weight": 70.5,
    "married": True,
    "address": address_info
}
patient = Patient(**patient_info)  # Create an instance of the Patient model

temp=patient.model_dump(exclude={'address':['state']})  # Serialize the model to a dictionary
print(temp)  # Print the serialized dictionary
print(type(temp))  # Print the type of the serialized dictionary

temp_json = patient.model_dump_json()  # Serialize the model to a JSON string
print(temp_json)  # Print the serialized JSON string
print(type(temp_json))  # Print the type of the serialized JSON string