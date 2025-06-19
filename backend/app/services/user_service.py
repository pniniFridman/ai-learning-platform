from sqlalchemy.orm import Session
from app.crud import user_crud # ייבוא פונקציות ה-CRUD עבור משתמשים
from app.schemas.user_schemas import UserCreate # ייבוא סכמת יצירת משתמש

def get_user_by_id(db: Session, user_id: int):
    """
    Service layer function to get a user by ID.
    """
    return user_crud.get_user(db, user_id)

def get_user_by_phone(db: Session, phone: str):
    """
    Service layer function to get a user by phone number.
    """
    return user_crud.get_user_by_phone(db, phone)

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Service layer function to get all users with pagination.
    """
    return user_crud.get_users(db, skip=skip, limit=limit)

def create_new_user(db: Session, user: UserCreate):
    """
    Service layer function to create a new user.
    Includes business logic like checking for existing phone number.
    """
    db_user = user_crud.get_user_by_phone(db, phone=user.phone)
    if db_user:
        # כאן ניתן לטפל בשגיאה, למשל להחזיר None או להרים HTTPException
        return None # לדוגמה, אם המשתמש כבר קיים
    return user_crud.create_user(db=db, user=user)

# (ניתן להוסיף כאן לוגיקה עסקית נוספת כמו אימות קלט מורכב יותר, או טיפול בהרשאות)