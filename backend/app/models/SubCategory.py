from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base # ודאי שהייבוא נכון

class SubCategory(Base):
    __tablename__ = "sub_categories" # שם הטבלה במסד הנתונים 

    id = Column(Integer, primary_key=True, index=True) # עמודת ID כמפתח ראשי 
    name = Column(String, index=True) # עמודת שם 
    category_id = Column(Integer, ForeignKey("categories.id")) # מפתח זר לטבלת categories 

    # יחס עם Category - תת-קטגוריה שייכת לקטגוריה אחת
    category = relationship("Category", back_populates="sub_categories")
    # יחס עם prompts - תת-קטגוריה יכולה להיות קשורה למספר פרומפטים
    prompts = relationship("Prompt", back_populates="sub_category")