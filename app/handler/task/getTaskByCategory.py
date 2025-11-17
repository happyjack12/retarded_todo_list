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


@router.get("WithLogin/category/", response_model=List[TaskRead], summary="Get Tasks by Category (Current User)")
def get_by_category(
    category: str = Query(..., description="Category to filter by"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> List[TaskRead]:
    tasks = get_tasks_by_category(db, category, user_id=current_user.id)
    return tasks