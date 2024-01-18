from sqlalchemy import Column, Integer, String, Boolean

from db import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    done = Column(Boolean, default=False)
