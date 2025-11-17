from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.user import User


def get_user_by_id_db(db: Session, name: str) -> Optional[User]:
    return db.query(User).filter(User.name == name).first()