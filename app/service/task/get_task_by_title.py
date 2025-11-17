from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task 
from app.repository.task.getTaskByTitle import get_task_by_title

def return_task_by_title(db: Session, title: str, user_id: int) -> Optional[Task]:
    return get_task_by_title(db, title, user_id)