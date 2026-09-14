from fastapi import APIRouter
from sqlalchemy import select
from app.database.connection import DbSession
from app.models.branches import Branch
from app.models.rooms import Room
from app.schemas.rooms import RoomCreate, GetRoom
from app.utils.checker import check_ident

router = APIRouter(tags=["Rooms"], prefix='/rooms')

@router.post("/", status_code=201)
async def post_room(rooms: RoomCreate, db: DbSession):

    await check_ident(db, Branch, rooms.branch_id)

    room = Room(
        **rooms.model_dump()
    )

    db.add(room)
    await db.commit()
    return "Room added"

@router.get("/", response_model=list[GetRoom])
async def get_rooms(db: DbSession, is_active: bool = True):
    result = await db.execute(select(Room))
    room = result.scalars().all()

    if is_active:
        room = await db.execute(select(Room).where(is_active == Room.is_active))

    return room

@router.delete("/{room_id}")
async def close_room(room_id: int, db: DbSession):

    room = await check_ident(db, Room, room_id)

    room.is_active = False

    await db.commit()
    return "Room closed!"
