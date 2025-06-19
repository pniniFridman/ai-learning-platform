from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user_schemas import User, UserCreate
from app.services import user_service
from app.database.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    db_user = user_service.get_user_by_phone(db, phone=user.phone)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone number already registered"
        )
    return user_service.create_new_user(db=db, user=user)

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