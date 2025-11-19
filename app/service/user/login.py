from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.core.logging_config import logging
from app.repository.user.get_user_by_email import get_user_by_email_db
from app.core.security import verify_password, create_access_token
from app.schemas.user import UserLogin, Token

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def login_user(db: Session, user_data: UserLogin) -> Token:
    logger.info(f"Попытка логина для email: {user_data.email}")
    user = get_user_by_email_db(db, email=user_data.email)

    if not user or not verify_password(user_data.password, user.hashed_password):
        
        if not user:
            logger.warning(f"Пользователь НЕ НАЙДЕН в DB для email: {user_data.email}")
        else:
            logger.warning(f"Пароль НЕ ВЕРНЫЙ для пользователя ID: {user.id}, email: {user_data.email}")
            
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неправильный email или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    logger.info(f"Логин УСПЕШЕН для пользователя ID: {user.id}")
    
    access_token = create_access_token(subject=str(user.id)) 

    return Token(access_token=access_token, token_type="bearer")