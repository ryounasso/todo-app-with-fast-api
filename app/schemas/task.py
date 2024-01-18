from pydantic import BaseModel, Field

class TaskCommon(BaseModel):
    name: str = Field("", example="買い出しに行く")
    done: bool = Field(False)

class Task(TaskCommon):
    id: int

    class Config:
        orm_mode = True

class TaskPost(BaseModel):
    name: str = Field("", example="買い出しに行く")

class TaskPostRes(BaseModel):
    id: int

    class Config:
        orm_mode = True
