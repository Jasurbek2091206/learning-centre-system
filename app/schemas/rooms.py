from pydantic import BaseModel

class RoomBase(BaseModel):
    branch_id: int
    name: str
    capacity: int

class RoomCreate(RoomBase):
    pass

class RoomUpdate(RoomBase):
    pass

class GetRoom(BaseModel):
    id: int
    branch_id: int
    name: str
    capacity: int
    is_active: bool