from sqlalchemy.orm import Session
from app.crud import category_crud
from app.schemas.category_schemas import CategoryCreate

def get_category_by_id(db: Session, category_id: int):
    """
    Service layer function to get a category by ID.
    """
    return category_crud.get_category(db, category_id)

def get_all_categories(db: Session, skip: int = 0, limit: int = 100):
    """
    Service layer function to get all categories.
    """
    return category_crud.get_categories(db, skip=skip, limit=limit)

def create_new_category(db: Session, category: CategoryCreate):
    """
    Service layer function to create a new category.
    """
    db_category = category_crud.get_category_by_name(db, name=category.name)
    if db_category:
        return None # Category already exists
    return category_crud.create_category(db=db, category=category)