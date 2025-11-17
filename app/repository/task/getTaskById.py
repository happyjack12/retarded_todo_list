from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task 


def get_task_by_id(db: Session, task_id: int, user_id: int) -> Optional[Task]:
    """Получает задачу по ID, принадлежащую конкретному пользователю."""
    # Добавляем фильтр по user_id
    return db.query(Task).filter(
        Task.id == task_id, 
        Task.user_id == user_id
    ).first()