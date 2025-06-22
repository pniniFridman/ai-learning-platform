# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from app.database.database import Base # חשוב לוודא שהייבוא נכון בהתאם למבנה התיקיות שלך

# class User(Base):
#     __tablename__ = "users" # שם הטבלה במסד הנתונים 

#     id = Column(Integer, primary_key=True, index=True) # עמודת ID כמפתח ראשי 
#     name = Column(String, index=True) # עמודת שם 
#     phone = Column(String, unique=True, index=True) # עמודת טלפון, עם ייחודיות 

#     # הגדרת היחס עם טבלת prompts
#     # user.prompts יחזיר רשימה של אובייקטי Prompt המשויכים למשתמש זה 
#     prompts = relationship("Prompt", back_populates="user")






    # backend/app/models/User.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False) # חובה, לא nullable
    phone = Column(String, unique=True, index=True, nullable=False) # חובה וייחודי
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    prompts = relationship("Prompt", back_populates="user")