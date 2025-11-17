import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User

from app.schemas.task import TaskRead, TaskCreate
from app.service.task.get_task import get_all_tasks, get_task_by_id, get_tasks_by_category, search_tasks_by_title

logger = logging.getLogger(__name__)
router = APIRouter(tags=["TASKS"], prefix="/tasks") 


@router.get("WithLogin/search/", response_model=List[TaskRead], summary="Search Tasks by Title (Current User)")
def search_tasks(
    title: str = Query(..., description="Title to search"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> List[TaskRead]:
    tasks = search_tasks_by_title(db, title, user_id=current_user.id)
    return tasks