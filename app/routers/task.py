from fastapi import APIRouter, Depends
from schemas.task import TaskPost, TaskPostRes, Task
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db
from cruds.task import add_task, get_task_list

router = APIRouter()

@router.get("/tasks", response_model=List[Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await get_task_list(db)


@router.post("/tasks", response_model=TaskPostRes)
async def create_task(request_body: TaskPost, db: AsyncSession = Depends(get_db)):
    return await add_task(db, request_body)

@router.put("/tasks/{task_id}")
async def update_task():
    pass
