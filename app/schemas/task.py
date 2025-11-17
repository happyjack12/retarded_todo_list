from typing import Optional

from pydantic import BaseModel, Field

from datetime import datetime

class TaskBase(BaseModel):
    title: str
    category: str

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    user_id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    category: Optional[str] = Field(None, min_length=1)