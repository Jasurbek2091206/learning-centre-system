from fastapi import APIRouter, status, HTTPException
from sqlalchemy import select
from app.database.connection import DbSession
from app.models.branches import Branch
from app.models.employee_roles import EmployeeRole
from app.models.employees import Employee
from app.models.roles import Role
from app.schemas.employee_roles import EmployeeRolesCreate, GetEmployeeRoles
from app.utils.checker import check_ident

router = APIRouter(tags=["Employee Roles"], prefix="/employee_roles")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_employee_role(emp_role: EmployeeRolesCreate, db: DbSession):
    result = await db.scalar(select(EmployeeRole).where(
        EmployeeRole.employee_id == emp_role.employee_id,
        EmployeeRole.branch_id == emp_role.branch_id,
        EmployeeRole.role_id == emp_role.role_id
    ))

    if result:
        raise HTTPException(409, "Employee already exists")

    await check_ident(db, Employee, emp_role.employee_id)
    await check_ident(db, Role, emp_role.role_id)
    await check_ident(db, Branch, emp_role.branch_id)

    obj = EmployeeRole(
        **emp_role.model_dump()
    )

    db.add(obj)

    await db.commit()
    return {"msg": "Employee role created successfully"}

@router.get("/", response_model=GetEmployeeRoles)
async def get_emmployee_role(db: DbSession):

    result = await db.execute(select(EmployeeRole))

    return result.scalars().all()
