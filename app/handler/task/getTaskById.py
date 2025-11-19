import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User

from app.schemas.task import TaskRead, TaskCreate
from app.service.task.get_task_by_id import return_task_by_id

logger = logging.getLogger(__name__)
router = APIRouter(tags=["TASKS"], prefix="/tasks") 


@router.get("WithLogin/{task_id}", response_model=TaskRead, summary="Get Task by ID (Current User)")
def get_by_id(
    task_id: int, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> TaskRead:
    task = return_task_by_id(db, task_id, user_id=current_user.id) 

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found or does not belong to the user"
        )
    return task