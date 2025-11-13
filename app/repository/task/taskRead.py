from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task

def get_all_tasks_db(db: Session) -> List[Task]:
    return db.query(Task).all()

def get_task_by_id_db(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks_by_category_db(db: Session, category: str) -> List[Task]:
    return db.query(Task).filter(Task.category == category).all()

def search_tasks_by_title_db(db: Session, title: str) -> List[Task]:
    return db.query(Task).filter(Task.title.contains(title)).all()