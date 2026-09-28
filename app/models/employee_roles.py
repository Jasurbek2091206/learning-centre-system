from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column
from app.database.base import Base
from app.models.employees import Employee
from app.models.roles import Role


class EmployeeRole(Base):
    __tablename__ = "employee_roles"
    employee_id: Mapped[int] = mapped_column(Integer, primary_key = True)
    role_id: Mapped[int] = mapped_column(Integer, primary_key = True)
    branch_id: Mapped[int] = mapped_column(Integer, ForeignKey("branches.id"))

    role: Mapped["Role"] = relationship("Role", back_populates="employee_roles")
    employee: Mapped["Employee"] = relationship("Employee", back_populates="employee_roles")
