from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
NAME = os.getenv("DB_NAME")

engine = create_async_engine(f"mysql+aiomysql://{USERNAME}:{PASSWORD}@localhost/{NAME}")

SessionLocal = async_sessionmaker(engine)

async def get_db():
    async with SessionLocal() as db:
        yield db

DbSession = Annotated[AsyncSession, Depends(get_db)]
