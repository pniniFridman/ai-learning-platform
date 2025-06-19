from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base # ודאי שהייבוא נכון

class Category(Base):
    __tablename__ = "categories" # שם הטבלה במסד הנתונים 

    id = Column(Integer, primary_key=True, index=True) # עמודת ID כמפתח ראשי 
    name = Column(String, unique=True, index=True) # עמודת שם, עם ייחודיות 

    # יחס עם sub_categories - קטגוריה יכולה להכיל מספר תתי-קטגוריות
    sub_categories = relationship("SubCategory", back_populates="category")
    # יחס עם prompts - קטגוריה יכולה להיות קשורה למספר פרומפטים
    prompts = relationship("Prompt", back_populates="category")