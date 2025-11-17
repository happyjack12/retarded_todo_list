from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task 


def get_all_tasks(db: Session, user_id: int) -> List[Task]:
    """Получает все активные задачи, принадлежащие конкретному пользователю."""
    return db.query(Task).filter(Task.user_id == user_id, Task.is_active == True).all()