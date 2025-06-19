from sqlalchemy.orm import Session
from app.models.User import User # ודאי שהייבוא נכון
from app.schemas.user_schemas import UserCreate # ודאי שהייבוא נכון

def get_user(db: Session, user_id: int):
    """
    Retrieves a user by ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_phone(db: Session, phone: str):
    """
    Retrieves a user by phone number.
    """
    return db.query(User).filter(User.phone == phone).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieves a list of users.
    """
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    """
    Creates a new user in the database.
    """
    db_user = User(name=user.name, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# (אפשר להוסיף פונקציות update_user ו-delete_user בהמשך אם נדרש)