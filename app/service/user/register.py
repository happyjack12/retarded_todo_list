from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repository.user.get_user_by_email import get_user_by_email_db
from app.repository.user.create_user import create_user
from app.schemas.user import UserCreate


def register_user(db: Session, user_data: UserCreate):
    user = get_user_by_email_db(db, email=user_data.email)

    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким email уже зарегистрирован"
        )
    
    new_user = create_user(
        db, 
        username=user_data.username, 
        email=user_data.email, 
        password=user_data.password 
    )
    
    return new_user