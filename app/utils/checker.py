from fastapi import HTTPException
from sqlalchemy import select


async def check_ident(db, model, ident):
    result = await db.execute(select(model).where(model.id == ident))
    obj = result.scalars().first()

    if not obj:
        raise HTTPException(404, "Object not found")

    return obj