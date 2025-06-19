from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base # חשוב לוודא שהייבוא נכון בהתאם למבנה התיקיות שלך

class User(Base):
    __tablename__ = "users" # שם הטבלה במסד הנתונים 

    id = Column(Integer, primary_key=True, index=True) # עמודת ID כמפתח ראשי 
    name = Column(String, index=True) # עמודת שם 
    phone = Column(String, unique=True, index=True) # עמודת טלפון, עם ייחודיות 

    # הגדרת היחס עם טבלת prompts
    # user.prompts יחזיר רשימה של אובייקטי Prompt המשויכים למשתמש זה 
    prompts = relationship("Prompt", back_populates="user")