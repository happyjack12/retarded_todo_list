from datetime import timedelta

from sqlalchemy.orm import Session

from app.repository.task.taskCreate import put_task
from app.schemas.task import TaskCreate


def create_task(db: Session, request: TaskCreate):
    return put_task(db, request)

