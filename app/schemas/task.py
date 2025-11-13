from typing import Optional

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    category: str = Field(..., min_length=1)

class TaskRead(BaseModel):
    id: int
    title: str
    category: str

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    category: Optional[str] = Field(None, min_length=1)