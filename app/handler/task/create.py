import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskRead
from app.service.task.create_task import create_task


logger = logging.getLogger(__name__)
router = APIRouter(tags=["TASKS"])


@router.post("/create", response_model=TaskRead, summary="Create Task")
def create(request: TaskCreate, db: Session = Depends(get_db)) -> TaskRead:
    new_task = create_task(db, request)
    return new_task


