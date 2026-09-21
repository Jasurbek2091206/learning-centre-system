from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from app.database.base import Base


class EmployeeRole(Base):
    __tablename__ = "employee_roles"
    employee_id: Mapped[int] = mapped_column(Integer, primary_key = True)
    role_id: Mapped[int] = mapped_column(Integer, primary_key = True)
    branch_id: Mapped[int] = mapped_column(Integer, ForeignKey("branches.id"))

    