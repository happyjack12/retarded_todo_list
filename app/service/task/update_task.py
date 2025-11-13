# app/service/task/update_task.py
from typing import Optional
from sqlalchemy.orm import Session
from app.models.task import Task
from app.repository.task.taskUpdate import change_task_title_category

def update_task(db: Session, task_id: int, title: Optional[str] = None, category: Optional[str] = None) -> Optional[Task]:
    return change_task_title_category(db, task_id, title, category)