from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.database import Base # ודאי שהייבוא נכון

class Prompt(Base):
    __tablename__ = "prompts" # שם הטבלה במסד הנתונים 

    id = Column(Integer, primary_key=True, index=True) # מפתח ראשי 
    user_id = Column(Integer, ForeignKey("users.id")) # מפתח זר למשתמש 
    category_id = Column(Integer, ForeignKey("categories.id")) # מפתח זר לקטגוריה 
    sub_category_id = Column(Integer, ForeignKey("sub_categories.id")) # מפתח זר לתת-קטגוריה 
    prompt = Column(Text) # טקסט הפרומפט שנשלח 
    response = Column(Text) # תגובת ה-AI 
    created_at = Column(DateTime, default=func.now()) # תאריך יצירה, ברירת מחדל היא הזמן הנוכחי 

    # הגדרת יחסים עם טבלאות אחרות
    user = relationship("User", back_populates="prompts") # יחס למשתמש
    category = relationship("Category", back_populates="prompts") # יחס לקטגוריה
    sub_category = relationship("SubCategory", back_populates="prompts") # יחס לתת-קטגוריה