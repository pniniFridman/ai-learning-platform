from sqlalchemy.orm import Session
from app.models.Category import Category # ודאי שהייבוא נכון
from app.schemas.category_schemas import CategoryCreate # ודאי שהייבוא נכון

def get_category(db: Session, category_id: int):
    """
    Retrieves a category by ID.
    """
    return db.query(Category).filter(Category.id == category_id).first()

def get_category_by_name(db: Session, name: str):
    """
    Retrieves a category by name.
    """
    return db.query(Category).filter(Category.name == name).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieves a list of categories.
    """
    return db.query(Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: CategoryCreate):
    """
    Creates a new category in the database.
    """
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category