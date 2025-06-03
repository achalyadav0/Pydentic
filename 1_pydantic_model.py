from pydantic import BaseModel, AnyUrl,  EmailStr, Field
from typing import List, Dict, Optional ,Annotated
# Annotated is used to add metadata to the fields of the model, such as validation constraints and descriptions
# BaseModel is the base class for all Pydantic models, it provides validation and serialization capabilities
#Field is used to define additional constraints on the fields of the model(custom data validation)
# AnyUrl is used to validate URLs, EmailStr is used to validate email addresses 
# Optional is used to indicate that a field can be None

class Patient(BaseModel): # this is a Pydantic model
    """A model representing a patient """  
    name: Annotated[str,Field(max_length=50,min_length=1,title="name of the patient",description="The name of the patient",example=["John Doe", "Jane Smith"])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: Annotated[int, Field(gt=0, le=120, description="The age of the patient in years")]
    # gt=0 means greater than 0, le=120 means less than or equal to 120
    weight: Annotated[float, Field(gt=0, strict=True,description="The weight of the patient in kilograms")]
    married: bool=False
    allergies: Annotated[List[str], Field(default=None,max_length=5, description="List of allergies the patient has")]
    contact_info: Dict[str, str]


# Function to insert a patient into a database
def insert_patient(patient: Patient):
    # Simulate inserting a patient into a database
    print(f"Inserting patient: {patient.name}, Email:{patient.email}, Linkedin_url:{patient.linkedin_url}, Age: {patient.age}, Weight: {patient.weight}, Married: {patient.married}, Allergies: {patient.allergies}, Contact Info: {','.join(patient.contact_info.values())}")

patient_info= {"name": "John Doe","email":'achallamba0@gmail.com',"linkedin_url":'http://linkedin.com/1234', "age": 30,"weight":70.8, "married":True,"contact_info":{"phone":"1234"}}  # Example patient data

patient1 = Patient(**patient_info)  # Create an instance of the Patient model

insert_patient(patient1)  # Insert the patient into the database