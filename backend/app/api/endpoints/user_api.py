# backend/app/api/endpoints/user_api.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Union, Dict, Any # הוספנו ייבוא של Union, Dict, Any

from app.schemas.user_schemas import User, UserCreate
from app.services import user_service
from app.database.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    print(f"Received user data in API endpoint: {user.model_dump_json()}")

    # שינוי הלוגיקה כדי להתאים למה ש-user_service.create_new_user מחזיר
    # נניח ש-create_new_user יכול להחזיר User (הצלחה) או Dict (שגיאה עם מפתח 'error')
    new_user_result: Union[User, Dict[str, Any]] = user_service.create_new_user(db=db, user=user)

    # נבדוק אם התוצאה היא מילון, ורק אז נחפש את מפתח 'error' בתוכו
    if isinstance(new_user_result, dict) and "error" in new_user_result:
        # טיפול בשגיאות שהוחזרו משכבת השירות (כמו בקוד המקורי)
        if new_user_result["error"] == "Email already registered":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        elif new_user_result["error"] == "Phone number already registered":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Phone number already registered"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An unexpected error occurred during user creation."
            )
    
    # אם אין שגיאה, new_user_result יהיה אובייקט User, ואותו נחזיר
    # המודל response_model=User ידאג לאימות והמרה
    return new_user_result

@router.get("/", response_model=List[User])
def read_users_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all users.
    """
    users = user_service.get_all_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=User)
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single user by ID.
    """
    user = user_service.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user