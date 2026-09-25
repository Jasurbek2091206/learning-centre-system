from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class TeacherProfile(Base):
    __tablename__ = "teacher_profiles"
    employee_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bio: Mapped[str] = mapped_column(Text, nullable=False)
    specialization: Mapped[str] = mapped_column(String(120), nullable=False)
    experience_years: Mapped[int] = mapped_column(Integer, nullable=False)
    max_groups: Mapped[int] = mapped_column(Integer, nullable=False)
