from datetime import date, datetime
from pydantic import BaseModel

class BranchBase(BaseModel):
    name: str
    code: str
    address: str
    phone: str
    city: str
    opened_at: date

class BranchCreate(BranchBase):
    pass

class BranchUpdate(BranchBase):
    pass

class GetBranch(BaseModel):
    id: int
    name: str
    code: str
    address: str
    phone: str
    city: str
    is_active: bool
    opened_at: date
    created_at: datetime