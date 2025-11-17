from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.models.user import User


def create_user(db: Session, username: str, email: str, password: str) -> Optional[User]:
    safe_password = password[:72]
    
    hashed_password = get_password_hash(safe_password)
    
    db_user = User(
        username=username, 
        email=email, 
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user