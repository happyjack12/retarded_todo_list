from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task 
from app.repository.task.getAllTasks import get_all_tasks

def return_all_tasks(db: Session, user_id: int) -> List[Task]:
    return get_all_tasks(db, user_id)
