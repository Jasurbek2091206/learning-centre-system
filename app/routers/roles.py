from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select

from app.database.connection import DbSession
from app.models.roles import Role
from app.schemas.roles import RoleCreate, GetRole, RoleUpdate
from app.utils.checker import check_ident
from app.utils.security import get_current_user

router = APIRouter(tags=["Roles"], prefix="/roles")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_role(db: DbSession, role: RoleCreate,
                    current_user = Depends(get_current_user)):

    result = await db.scalar(select(Role).where(Role.code == role.code))

    if result:
        raise HTTPException(409, "This code already exists")

    obj = Role(
        **role.model_dump()
    )

    db.add(obj)
    await db.commit()
    return {"msg": "Role created successfully"}

@router.get("/", response_model=list[GetRole])
async def get_roles(db: DbSession):
    result = await db.execute(select(Role))
    return result.scalars().all()

@router.put("/{role_id}")
async def put_role(role_id: int, db: DbSession, role: RoleUpdate,
                   current_user = Depends(get_current_user)):
    result = await check_ident(db, Role, role_id)

    code = await db.scalar(select(Role).where(Role.code == role.code))

    if code:
        raise HTTPException(409, "Code already exist")

    result.code = role.code
    result.name = role.name
    await db.commit()

    return {"msg": "Role updated successfully"}

@router.delete("/{role_id}")
async def remove_role(db: DbSession, role_id: int, current_user = Depends(get_current_user)):

    role = await check_ident(db, Role, role_id)

    if not role:
        raise HTTPException(404, "Role not found")

    await db.delete(role)
    await db.commit()
    return {"msg": "Role deleted"}


