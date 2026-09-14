from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.database.connection import DbSession
from app.models.branches import Branch
from app.schemas.branches import BranchCreate, GetBranch, BranchUpdate
from app.utils.checker import check_ident

router = APIRouter(tags=["Branches"], prefix='/branch')

@router.post("/", status_code=201)
async def post_branch(branches: BranchCreate, db: DbSession):

    branch_code = await db.scalar(select(Branch).where(branches.code == Branch.code))

    if branch_code:
        raise HTTPException(409, "Bu koddagi filial allaqachon mavjud")

    branch = Branch(
        **branches.model_dump()
    )

    db.add(branch)
    await db.commit()

    return "Yangi filial qo'shildi 🎉"

@router.get("/", response_model=list[GetBranch])
async def get_branches(db: DbSession):
    branches = await db.execute(select(Branch))
    result = branches.scalars().all()
    return result

@router.put("/{branch_id}")
async def update_branch(branch_id: int, branches: BranchUpdate, db: DbSession):

    branch = await check_ident(db, Branch, branch_id)

    branch.name = branches.name
    branch.code = branches.code
    branch.address = branches.address
    branch.phone = branches.phone
    branch.city = branches.city

    await db.commit()
    return "Branch updated"

@router.delete("/{branch_id}")
async def stop_branch(branch_id: int, db: DbSession):

    branch = await check_ident(db, Branch, branch_id)

    branch.is_active = False

    await db.commit()
    return "Branch closed successfully!"

