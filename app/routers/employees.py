from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.database.connection import DbSession
from app.models.branches import Branch
from app.models.employees import Employee
from app.schemas.employees import EmployeeCreate, GetEmployee, EmployeeUpdate
from app.utils.checker import check_ident
from app.utils.security import get_password_hash

router = APIRouter(tags=["Employees"], prefix="/employees")

@router.post("/", status_code=201)
async def post_employee(employee: EmployeeCreate, db: DbSession):
    await check_ident(db, Branch, employee.branch_id)

    result = await db.execute(select(Employee).where(Employee.phone == employee.phone))
    user = result.scalars().first()

    if user:
        raise HTTPException(409, "This user already exists")

    obj = Employee(
        **employee.model_dump(exclude={"password"}),
        password = await get_password_hash(employee.password)
    )

    db.add(obj)
    await db.commit()

    return "Employee created successfully"

@router.get("/", response_model=list[GetEmployee])
async def get_employee(db: DbSession, is_acvtive: bool = True):

    result = await db.execute(select(Employee).where(is_acvtive == Employee.is_active))

    return result.scalars().all()

@router.put("/{employee_id}")
async def put_employee(employee_id: int, employee: EmployeeUpdate, db: DbSession):
    emp = await check_ident(db, Employee, employee_id)

    if not emp.is_active:
        raise HTTPException(400, "Employee does not active")

    await check_ident(db, Branch, employee.branch_id)

    # result = await db.execute(select(Employee).where(Employee.phone == employee.phone))
    # user = result.scalars().all()
    #
    # if user:
    #     raise HTTPException(409, "Employee already exists")

    update_data = employee.model_dump(exclude_unset=True)

    update_data["password"] = await get_password_hash(update_data["password"])

    for field, value in update_data.items():
        setattr(emp, field, value)

    await db.commit()
    return "Employe updated successfully"

@router.patch("/{employee_id}")
async def toggle_employye_status(employee_id: int, db : DbSession):
    emp = await check_ident(db, Employee, employee_id)
    emp.is_active = True
    emp.fired_at = None
    await db.commit()

    return "Employee status updated successfully"

@router.delete("/{employee_id}")
async def delete_employee(employee_id: int, db: DbSession):
    emp = await check_ident(db, Employee, employee_id)

    emp.is_active = False
    emp.fired_at = datetime.now(timezone.utc)

    await db.commit()
    return "Employee soft deleted"

