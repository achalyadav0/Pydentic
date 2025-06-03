from pydantic import BaseModel, Field, ValidationError, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional, Annotated

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool 
    allergies: List[str]
    contact_info: Dict[str, str]
    address: Address

address_info = {
    "street": "123 Main St",
    "city": "Springfield",
    "state": "IL",
    "zip_code": "62701"
}
address = Address(**address_info)


patient_info = {
    "name": "achal yadav",
    "email": "achallamba@gmail.com",
    "age": 34,
    "weight": 70.5,
    "height": 1.72 , 
    "married": True,        
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {"phone": "123-456-7890", "address": "123 Main St",'emergency_contact': '9876543210'},
    "address": address_info
}

  # Create an instance of the Patient model
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.address)
    print("Patient data updated successfully.")
patient=Patient(**patient_info)
update_patient_data(patient)  # Update the patient data