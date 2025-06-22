# from sqlalchemy.orm import Session
# from app.models.User import User # ודאי שהייבוא נכון
# from app.schemas.user_schemas import UserCreate # ודאי שהייבוא נכון

# def get_user(db: Session, user_id: int):
#     """
#     Retrieves a user by ID.
#     """
#     return db.query(User).filter(User.id == user_id).first()

# def get_user_by_phone(db: Session, phone: str):
#     """
#     Retrieves a user by phone number.
#     """
#     return db.query(User).filter(User.phone == phone).first()

# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     """
#     Retrieves a list of users.
#     """
#     return db.query(User).offset(skip).limit(limit).all()

# def create_user(db: Session, user: UserCreate):
#     """
#     Creates a new user in the database.
#     """
#     db_user = User(name=user.name, phone=user.phone)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# # (אפשר להוסיף פונקציות update_user ו-delete_user בהמשך אם נדרש)





# backend/app/crud/user_crud.py
from sqlalchemy.orm import Session
from app.models.User import User
from app.schemas.user_schemas import UserCreate
from app.core.security import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_phone(db: Session, phone: str): # פונקציה זו חשובה כעת לבדיקת ייחודיות
    return db.query(User).filter(User.phone == phone).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    
    # יוצרים את המשתמש עם כל הנתונים שהתקבלו
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        name=user.name,
        phone=user.phone,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user