from typing import Optional

from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate

from app.models.task import Task


def change_task_title_category(db: Session, task_id: int, title: Optional[str] = None, category: Optional[str] = None) -> Optional[Task]:
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        return None
    
    if title is not None:
        db_task.title = title
    if category is not None:
       db_task.category = category
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task