from datetime import datetime
from datetime import date
from pydantic import BaseModel, EmailStr


class EmployeeBase(BaseModel):
    branch_id: int
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    password: str
    birth_date: date
    photo_url: str
    position: str
    hired_at: date

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class GetEmployee(BaseModel):
    id: int
    branch_id: int
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    password: str
    birth_date: date
    photo_url: str
    position: str
    hired_at: date
    fired_at: date | None
    is_active: bool
    created_at: datetime
    updated_at: datetime