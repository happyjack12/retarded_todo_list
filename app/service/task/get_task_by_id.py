from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task 
from app.repository.task.getTaskById import get_task_by_id

def return_task_by_id(db: Session, task_id: int, user_id: int) -> Optional[Task]:
    return get_task_by_id(db, task_id, user_id)