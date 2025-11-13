from sqlalchemy.orm import Session
from app.models.task import Task

def delete_task_db(db: Session, task_id: int) -> bool:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return False
    
    db.delete(task)
    db.commit()
    return True