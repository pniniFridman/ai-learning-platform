from sqlalchemy.orm import Session
from app.crud import sub_category_crud, category_crud # נצטרך את category_crud כדי לוודא קטגוריה קיימת
from app.schemas.sub_category_schemas import SubCategoryCreate

def get_sub_category_by_id(db: Session, sub_category_id: int):
    """
    Service layer function to get a sub-category by ID.
    """
    return sub_category_crud.get_sub_category(db, sub_category_id)

def get_sub_categories_for_category(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    """
    Service layer function to get sub-categories for a specific category.
    """
    return sub_category_crud.get_sub_categories_by_category(db, category_id, skip=skip, limit=limit)

def create_new_sub_category(db: Session, sub_category: SubCategoryCreate):
    """
    Service layer function to create a new sub-category.
    Includes business logic like checking if parent category exists.
    """
    # ודא שהקטגוריה הראשית קיימת
    parent_category = category_crud.get_category(db, sub_category.category_id)
    if not parent_category:
        return None # Parent category does not exist, cannot create sub-category

    # ודא שתת-קטגוריה עם אותו שם לא קיימת כבר תחת אותה קטגוריה
    # (זו בדיקה מורכבת יותר שתצריך פונקציה נוספת ב-CRUD או לוגיקה כאן)

    return sub_category_crud.create_sub_category(db=db, sub_category=sub_category)