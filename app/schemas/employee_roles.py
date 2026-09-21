from pydantic import BaseModel

class EmployeeRoleBase(BaseModel):
    employee_id: int
    role_id: int
    branch_id: int

class EmployeeRolesCreate(EmployeeRoleBase):
    pass

class EmployeeRolesUpdate(EmployeeRoleBase):
    pass

class GetEmployeeRoles(EmployeeRoleBase):
    pass