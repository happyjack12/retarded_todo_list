from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task 


def get_tasks_by_category(db: Session, category: str, user_id: int) -> List[Task]:
    """Получает задачи по категории, принадлежащие конкретному пользователю."""
    # Добавляем фильтр по user_id
    return db.query(Task).filter(
        Task.category == category, 
        Task.user_id == user_id,
        Task.is_active == True
    ).all()
