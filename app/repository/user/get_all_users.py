from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.user import User

def get_all_users_db(db: Session) -> List[User]:
    return db.query(User).all()