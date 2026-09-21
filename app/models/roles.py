from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    is_system: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
