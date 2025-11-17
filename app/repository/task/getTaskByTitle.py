from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task 


def get_task_by_title(db: Session, title: str, user_id: int) -> List[Task]:
    return db.query(Task).filter(
        Task.title.contains(title),
        Task.user_id == user_id,
        Task.is_active == True
    ).all()