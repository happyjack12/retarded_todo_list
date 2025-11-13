# app/handler/task/update.py
import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.task import TaskRead, TaskUpdate
from app.service.task.update_task import update_task

logger = logging.getLogger(__name__)
router = APIRouter(tags=["TASKS"])

@router.put("/{task_id}", response_model=TaskRead, summary="Update Task")
def update_task_handler(
    task_id: int, 
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
) -> TaskRead:
    updated_task = update_task(
        db, 
        task_id, 
        title=task_data.title, 
        category=task_data.category
    )
    
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    
    return updated_task