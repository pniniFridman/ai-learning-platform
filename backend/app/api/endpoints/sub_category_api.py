from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.sub_category_schemas import SubCategory, SubCategoryCreate
from app.services import sub_category_service
from app.database.database import get_db

router = APIRouter(prefix="/sub-categories", tags=["Sub-Categories"])

@router.post("/", response_model=SubCategory, status_code=status.HTTP_201_CREATED)
def create_sub_category_endpoint(sub_category: SubCategoryCreate, db: Session = Depends(get_db)):
    """
    Create a new sub-category.
    """
    db_sub_category = sub_category_service.create_new_sub_category(db=db, sub_category=sub_category)
    if db_sub_category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create sub-category. Check if parent category exists or name is duplicate."
        )
    return db_sub_category

@router.get("/", response_model=List[SubCategory])
def read_sub_categories_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all sub-categories.
    """
    sub_categories = sub_category_service.get_all_sub_categories(db, skip=skip, limit=limit)
    return sub_categories

@router.get("/by-category/{category_id}", response_model=List[SubCategory])
def read_sub_categories_by_category_endpoint(category_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve sub-categories filtered by a specific category ID.
    """
    sub_categories = sub_category_service.get_sub_categories_for_category(db, category_id=category_id, skip=skip, limit=limit)
    return sub_categories

@router.get("/{sub_category_id}", response_model=SubCategory)
def read_sub_category_endpoint(sub_category_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single sub-category by ID.
    """
    sub_category = sub_category_service.get_sub_category_by_id(db, sub_category_id=sub_category_id)
    if sub_category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sub-Category not found")
    return sub_category