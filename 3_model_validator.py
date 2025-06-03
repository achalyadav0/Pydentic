from pydantic import BaseModel, Field, ValidationError, EmailStr, AnyUrl, field_validator, model_validator,computed_field
from typing import List, Dict, Optional, Annotated

# model_validator is used to validate the entire model after all fields have been validated, it is a class method that takes the model instance as an argument and returns the validated model or raises a ValueError if the validation fails.

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: Annotated[float, Field(gt=0, description="Height in meters")]
    married: bool
    allergies: List[str]
    contact_info: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model) :
        if model.age>60 and 'emergency_contact' not in model.contact_info:
            raise ValueError("Emergency contact is required for patients over 60 years old")
        return model

    @computed_field
    @property
    def bmi(self) -> float:
        """Calculate Body Mass Index (BMI)"""
        return round(self.weight / (self.height ** 2),2) 

    

patient_info = {
    "name": "achal yadav",
    "email": "achallamba@gmail.com",
    "age": 34,
    "weight": 70.5,
    "height": 1.72 , 
    "married": True,        
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {"phone": "123-456-7890", "address": "123 Main St",'emergency_contact': '9876543210'}
}

  # Create an instance of the Patient model
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(f"Patient BMI: {patient.bmi}")
    print("Patient data updated successfully.")
patient=Patient(**patient_info)
update_patient_data(patient)  # Update the patient data