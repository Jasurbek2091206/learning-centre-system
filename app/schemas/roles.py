from pydantic import BaseModel

class RoleBase(BaseModel):
    code: str
    name: str

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleResponse(BaseModel):
    id: int
    code: str
    name: str
    is_system: bool
