# Pydentic

This repository contains Python examples demonstrating how to use [Pydantic](https://docs.pydantic.dev/) for data modeling and serialization.

## Features

- Define data models using Pydantic's `BaseModel`
- Nested models (e.g., `Patient` with an `Address`)
- Serialization to dictionary and JSON
- Field exclusion during serialization

## Example

The main example is in `5_serialization.py`:

```python
from pydantic import BaseModel

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
    address: Address

# Create and serialize a Patient instance
```

## How to Run

1. Install dependencies:
    ```bash
    pip install pydantic
    ```

2. Run the example:
    ```bash
    python 5_serialization.py
    ```

## Output

- Prints the serialized dictionary (with excluded fields)
- Prints the serialized JSON string

---
