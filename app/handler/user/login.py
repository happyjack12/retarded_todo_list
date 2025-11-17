import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserLogin, Token
from app.service.user.login import login_user


logger = logging.getLogger(__name__)
router = APIRouter(tags=["AUTH"], prefix="/auth")

@router.post("/login", response_model=Token, summary="User Login")
def login(request: UserLogin, db: Session = Depends(get_db)) -> Token:
    token = login_user(db, user_data=request)
    return token