from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from app.database.connection import DbSession
from app.models.employees import Employee
from app.schemas.auth import RefreshToken
from app.utils.security import verify_password, create_access_token, craete_refresh_token, create_new_access_token

router = APIRouter(tags=["Auth"], prefix="/auth")

@router.post("/login", status_code=201)
async def login(db: DbSession, user_data: OAuth2PasswordRequestForm = Depends()):
    result = await db.execute(select(Employee). where(Employee.phone == user_data.username))
    employee = result.scalars().first()

    if not employee:
        raise HTTPException(401, "Phone or password incorrect")


    if not employee or not await verify_password(user_data.password, employee.password):
        raise HTTPException(401, "Phone or password incorrect")

    acc_token = await create_access_token(employee.id)
    ref_token = await craete_refresh_token(employee.id)

    return {
        "access token": acc_token,
        "refresh token": ref_token,
        "token type": "bearer",
    }

@router.post("/refresh", status_code=201)
async def refresh(token: RefreshToken, db: DbSession):
    return await create_new_access_token(token.refresh_token, db)
