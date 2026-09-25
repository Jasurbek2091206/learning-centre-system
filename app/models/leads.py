# from datetime import datetime, timezone
# from sqlalchemy import Integer, ForeignKey, String, Text, DateTime
# from sqlalchemy.orm import Mapped, mapped_column
# from app.database.base import Base
#
#
# class Leads(Base):
#     __tablename__ = "leads"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     branch_id: Mapped[int] = mapped_column(Integer, ForeignKey("branches.id"))
#     first_name: Mapped[str] = mapped_column(String(60), nullable=False)
#     last_name: Mapped[str] = mapped_column(String(60), nullable=False)
#     phone: Mapped[str] = mapped_column(String(20), nullable=False)
#     source_id: Mapped[int] = mapped_column(Integer, ForeignKey("sources.id"), nullable=False)
#     status_id: Mapped[int] = mapped_column(Integer, ForeignKey("status.id"), nullable=False)
#     course_id: Mapped[int] = mapped_column(Integer, ForeignKey("courses.id"), nullable=False)
#     assigned_to: Mapped[int] = mapped_column(Integer, ForeignKey(""), nullable=False)
#     lost_reason: Mapped[str] = mapped_column(String(200), nullable=False)
#     student_id: Mapped[int] = mapped_column(Integer, nullable=False)
#     comment: Mapped[str] = mapped_column(Text, nullable=False)
#     created_by:
#     updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
#
