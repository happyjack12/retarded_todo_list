from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

from app.core.config import get_settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверяет соответствие открытого пароля его хешу, обрезая его до 72 символов."""
    safe_password = plain_password[:72]
    return pwd_context.verify(safe_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Создает хеш для заданного пароля."""
    return pwd_context.hash(password)


def create_access_token(*, subject: str, expires_delta: Optional[timedelta] = None) -> str:
    """Генерирует JWT токен доступа."""
    settings = get_settings()
    expire = datetime.now(timezone.utc) + (
        expires_delta if expires_delta else timedelta(minutes=settings.access_token_expire_minutes)
    )
    to_encode = {"sub": subject, "exp": expire.isoformat()} 
    return jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)