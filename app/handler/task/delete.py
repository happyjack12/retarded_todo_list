# app/handler/task/update.py
import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.service.task.delete_task import delete_task

logger = logging.getLogger(__name__)
router = APIRouter(tags=["TASKS"])

@router.delete("/{task_id}", summary="Delete Task")
def delete_task_handler(task_id: int, db: Session = Depends(get_db)):
    success = delete_task(db, task_id)
    if not success:
        raise HTTPException(404, f"Task {task_id} not found")
    return {"message": "Task deleted successfully"}