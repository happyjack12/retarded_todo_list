import logging

from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer as OAuth2
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.config import get_settings 
from app.models.user import User
from app.repository.user.get_user_by_id import get_user_by_id_db


logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2(tokenUrl="auth/login") 

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Security(oauth2_scheme)
) -> User:
    """
    Проверяет JWT токен, декодирует ID пользователя и возвращает объект User.
    """
    settings = get_settings()
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(
            token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm]
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        
    except JWTError:
        raise credentials_exception

    user = get_user_by_id_db(db, int(user_id))

    if user is None or not user.is_active:
        raise credentials_exception
    
    return user