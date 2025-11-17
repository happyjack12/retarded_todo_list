import logging
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User

from app.schemas.task import TaskRead, TaskCreate
from app.service.task.create_task_with_user import create_task

logger = logging.getLogger(__name__)
router = APIRouter(tags=["TASKS"], prefix="/tasks") 

@router.post("/WithLogin", response_model=TaskRead, status_code=status.HTTP_201_CREATED, summary="Create New Task")
def create_new_task(
    request: TaskCreate, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> TaskRead:
    new_task = create_task(db, request, user_id=current_user.id)
    return new_task