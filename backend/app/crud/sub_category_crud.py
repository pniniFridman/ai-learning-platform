from sqlalchemy.orm import Session
from app.models.SubCategory import SubCategory # ודאי שהייבוא נכון
from app.schemas.sub_category_schemas import SubCategoryCreate # ודאי שהייבוא נכון

def get_sub_category(db: Session, sub_category_id: int):
    """
    Retrieves a sub-category by ID.
    """
    return db.query(SubCategory).filter(SubCategory.id == sub_category_id).first()

def get_sub_categories_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    """
    Retrieves sub-categories by category ID.
    """
    return db.query(SubCategory).filter(SubCategory.category_id == category_id).offset(skip).limit(limit).all()

def create_sub_category(db: Session, sub_category: SubCategoryCreate):
    """
    Creates a new sub-category in the database.
    """
    db_sub_category = SubCategory(name=sub_category.name, category_id=sub_category.category_id)
    db.add(db_sub_category)
    db.commit()
    db.refresh(db_sub_category)
    return db_sub_category