import os
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException
from jose import jwt, ExpiredSignatureError, JWTError
from passlib.context import CryptContext
from dotenv import load_dotenv
from app.models.employees import Employee
from app.utils.checker import check_ident

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

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

async def craete_refresh_token(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
        "type": "refresh"
    }

async def create_new_access_token(token: str, db) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

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