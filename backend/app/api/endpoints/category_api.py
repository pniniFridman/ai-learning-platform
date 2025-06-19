from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.category_schemas import Category, CategoryCreate
from app.services import category_service
from app.database.database import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_db)):
    """
    Create a new category.
    """
    db_category = category_service.create_new_category(db=db, category=category)
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category with this name already exists"
        )
    return db_category

@router.get("/", response_model=List[Category])
def read_categories_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all categories.
    """
    categories = category_service.get_all_categories(db, skip=skip, limit=limit)
    return categories

@router.get("/{category_id}", response_model=Category)
def read_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single category by ID.
    """
    category = category_service.get_category_by_id(db, category_id=category_id)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category