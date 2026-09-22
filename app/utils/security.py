from datetime import datetime, timezone, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, ExpiredSignatureError, JWTError
from passlib.context import CryptContext
from sqlalchemy import select
from app.database.connection import DbSession
from app.models.employees import Employee
from app.utils.checker import check_ident
from app.utils.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

pwd_context = CryptContext(schemes=["argon2"])


async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def create_access_token(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
        "type": "access"
    }

    return jwt.encode(payload, SECRET_KEY, ALGORITHM)


async def create_refresh_token(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
        "type": "refresh"
    }

    return jwt.encode(payload, SECRET_KEY, ALGORITHM)


async def create_new_access_token(token: str, db) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload["type"] != "refresh":
            raise HTTPException(400, "No refresh token")

        user_id = payload["user_id"]

        user = await check_ident(db, Employee, user_id)

        return {
            "New access token": await create_access_token(user.id)
        }
    except ExpiredSignatureError:
        raise HTTPException(401, "Token is expired")
    except JWTError:
        raise HTTPException(401, "Token invalid")


bearer = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(db: DbSession, token = Depends(bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(401, detail="Token ichida user_id topilmadi")
    except JWTError:
        raise HTTPException(401, "Token yaroqsiz yoki muddati tugagan")

    result = await db.execute(select(Employee).where(Employee.id == user_id))
    user_data = result.scalars().all()

    if not user_data:
        raise HTTPException(404, "Foydalanuvchi topilmadi")

    return user_data