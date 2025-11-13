from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task
from app.repository.task.taskRead import get_all_tasks_db, get_task_by_id_db, get_tasks_by_category_db, search_tasks_by_title_db

def get_all_tasks(db: Session) -> List[Task]:
    return get_all_tasks_db(db)

def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
    return get_task_by_id_db(db, task_id)

def get_tasks_by_category(db: Session, category: str) -> List[Task]:
    return get_tasks_by_category_db(db, category)

def search_tasks_by_title(db: Session, title: str) -> List[Task]:
    return search_tasks_by_title_db(db, title)