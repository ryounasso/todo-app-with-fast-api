from fastapi import APIRouter
import schemas.task as task_scheme
from typing import List

router = APIRouter()


@router.get("/tasks", response_model=List[task_scheme.Task])
async def list_tasks():
    return [task_scheme.Task(id=1, title="クリーニングを取りに行く", done=False)]


@router.post("/tasks", response_model=task_scheme.TaskCreateResponse)
async def create_task(task_body: task_scheme.TaskCreate):
    return task_scheme.TaskCreateResponse(id=1, title=task_body.title)


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass