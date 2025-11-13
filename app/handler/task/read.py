import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.task import TaskRead
from app.service.task.get_task import get_all_tasks, get_task_by_id, get_tasks_by_category, search_tasks_by_title

logger = logging.getLogger(__name__)
router = APIRouter(tags=["TASKS"])

@router.get("/", response_model=List[TaskRead], summary="Get All Tasks")
def get_all(db: Session = Depends(get_db)) -> List[TaskRead]:
    tasks = get_all_tasks(db)
    return tasks

@router.get("/{task_id}", response_model=TaskRead, summary="Get Task by ID")
def get_by_id(task_id: int, db: Session = Depends(get_db)) -> TaskRead:
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task

@router.get("/category/{category}", response_model=List[TaskRead], summary="Get Tasks by Category")
def get_by_category(category: str, db: Session = Depends(get_db)) -> List[TaskRead]:
    tasks = get_tasks_by_category(db, category)
    return tasks

@router.get("/search/", response_model=List[TaskRead], summary="Search Tasks by Title")
def search_tasks(
    title: str = Query(..., description="Title to search"),
    db: Session = Depends(get_db)
) -> List[TaskRead]:
    tasks = search_tasks_by_title(db, title)
    return tasks