import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User

from app.schemas.task import TaskRead, TaskCreate
from app.service.task.get_all_tasks import return_all_tasks

logger = logging.getLogger(__name__)
router = APIRouter(tags=["TASKS"], prefix="/tasks") 


@router.get("/WithLogin", response_model=List[TaskRead], summary="Get All Tasks for Current User")
def get_all(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> List[TaskRead]:
    tasks = return_all_tasks(db, user_id=current_user.id)
    return tasks
