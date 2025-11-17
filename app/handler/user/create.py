import logging

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserRead
from app.service.user.register import register_user


logger = logging.getLogger(__name__)
router = APIRouter(tags=["AUTH"], prefix="/auth")


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED, summary="Register New User")
def register(request: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    new_user = register_user(db, user_data=request)
    return new_user