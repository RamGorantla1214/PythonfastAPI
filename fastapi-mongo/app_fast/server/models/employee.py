from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class EmployeeSchema(BaseModel):
    full_name: str = Field(...)
    email_id: EmailStr = Field(...)
    role: str = Field(...)
    year_of_experience: str = Field(...)
    salary: float = Field(..., ge=0)

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Thor",
                "email_id": "thor@x.edu.ng",
                "role": "actor",
                "year_of_experience": 20,
                "salary": "3000000",
            }
        }


class UpdateEmployeeModel(BaseModel):
    full_name: Optional[str]
    email_id: Optional[EmailStr]
    role: Optional[str]
    year_of_experience: Optional[int]
    salary: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Thor",
                "email_id": "thor@x.edu.ng",
                "role": "actor",
                "year_of_experience": 20,
                "salary": "3000000",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}


