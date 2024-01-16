from typing import Optional
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from pydantic import Field

from routers import task, done

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class ShopInfo(BaseModel):
    name: str
    location: str

class Data(BaseModel):
    shop: ShopInfo
    item: List[Item]

app = FastAPI()

app.include_router(task.router)
app.include_router(done.router)

@app.post("/items/")
def create_item(item: Data):
    return item