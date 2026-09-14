from fastapi import FastAPI
from app.routers.branches import router as branch_router
from app.routers.rooms import router as room_router
from app.routers.employees import router as employee_router

app = FastAPI(title="Learning Centre", docs_url="/")

app.include_router(branch_router)
app.include_router(room_router)
app.include_router(employee_router)

