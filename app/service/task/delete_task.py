from sqlalchemy.orm import Session
from app.repository.task.taskDelete import delete_task_db

def delete_task(db: Session, task_id: int) -> bool:
    return delete_task_db(db, task_id)