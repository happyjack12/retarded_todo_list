from sqlalchemy.orm import Session

from app.repository.task.taskCreateWithUser import put_task
from app.schemas.task import TaskCreate


def create_task(db: Session, request: TaskCreate, user_id: int):
    return put_task(db, request, user_id)