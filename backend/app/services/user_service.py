# backend/app/services/user_service.py
from sqlalchemy.orm import Session
from app.crud import user_crud
from app.schemas.user_schemas import UserCreate

def get_user_by_id(db: Session, user_id: int):
    return user_crud.get_user(db, user_id)

def get_user_by_email(db: Session, email: str):
    return user_crud.get_user_by_email(db, email)

def get_user_by_phone(db: Session, phone: str):
    return user_crud.get_user_by_phone(db, phone)

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return user_crud.get_users(db, skip=skip, limit=limit)

def create_new_user(db: Session, user: UserCreate):
    """
    Service layer function to create a new user.
    Includes business logic like checking for existing email/phone.
    """
    db_user_email = user_crud.get_user_by_email(db, email=user.email)
    if db_user_email:
        return {"error": "Email already registered"} # נחזיר שגיאה מסוג ספציפי
            
    db_user_phone = user_crud.get_user_by_phone(db, phone=user.phone)
    if db_user_phone:
        return {"error": "Phone number already registered"} # נחזיר שגיאה מסוג ספציפי

    return user_crud.create_user(db=db, user=user)