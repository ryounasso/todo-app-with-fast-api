from sqlalchemy.ext.asyncio import AsyncSession

from models.task import TaskModel
from schemas.task import TaskPost, Task
from sqlalchemy import select

from typing import List, Tuple

async def get_task_list(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    tasks = await db.execute(
        select(TaskModel.id, TaskModel.name, TaskModel.done)
    )
    return tasks.all()

async def add_task(
    db: AsyncSession, task_create: TaskPost
) -> TaskModel:
    task = TaskModel(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task