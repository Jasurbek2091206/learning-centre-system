from datetime import date, datetime, timezone
from sqlalchemy import Integer, ForeignKey, String, Date, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class Employee(Base):
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    branch_id: Mapped[int] = mapped_column(Integer, ForeignKey("branches.id"))
    first_name: Mapped[str] = mapped_column(String(60), nullable=False)
    last_name: Mapped[str] = mapped_column(String(60), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)
    photo_url: Mapped[str] = mapped_column(String(255), nullable=False)
    position: Mapped[str] = mapped_column(String(80), nullable=False)
    hired_at: Mapped[date] = mapped_column(Date, nullable=False)
    fired_at: Mapped[date] = mapped_column(Date, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now(timezone.utc))


