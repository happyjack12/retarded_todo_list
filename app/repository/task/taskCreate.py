from typing import Optional

from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate

from app.models.task import Task


def put_task(db: Session, task_data: TaskCreate) -> Optional[Task]:
    db_task = Task(title = task_data.title, category = task_data.category)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return task_data

