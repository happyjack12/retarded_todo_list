from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repository.user.get_user_by_email import get_user_by_email_db
from app.core.security import verify_password, create_access_token
from app.schemas.user import UserLogin, Token


def login_user(db: Session, user_data: UserLogin) -> Token:
    user = get_user_by_email_db(db, email=user_data.email)

    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неправильный email или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(subject=str(user.id)) 

    return Token(access_token=access_token, token_type="bearer")