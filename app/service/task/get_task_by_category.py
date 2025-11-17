from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task 
from app.repository.task.getTaskByCategory import get_tasks_by_category

def return_task_by_category(db: Session,  category: str, user_id: int) -> Optional[Task]:
    return get_tasks_by_category(db, category, user_id)