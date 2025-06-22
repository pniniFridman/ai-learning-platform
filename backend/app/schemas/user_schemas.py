# from pydantic import BaseModel, Field
# from typing import Optional

# # Schema לבסיס המשתמש - שדות משותפים
# class UserBase(BaseModel):
#     name: str = Field(..., example="John Doe")
#     phone: str = Field(..., example="0501234567")

# # Schema ליצירת משתמש (כולל שדות שניתן להזין ביצירה)
# class UserCreate(UserBase):
#     pass # כרגע אין שדות נוספים מעבר ל-UserBase ביצירה

# # Schema לתגובת API עבור משתמש (כולל שדה ה-ID שנוצר על ידי DB)
# class User(UserBase):
#     id: int = Field(..., example=1)

#     class Config:
#         from_attributes = True # או orm_mode = True בגרסאות Pydantic ישנות יותר
#         # מאפשר ל-Pydantic לקרוא נתונים מאובייקטי ORM






        # backend/app/schemas/user_schemas.py
from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    email: str = Field(..., example="john.doe@example.com")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
    name: str = Field(..., min_length=1, max_length=100, example="John Doe") # חובה
    phone: str = Field(..., min_length=7, max_length=20, example="0501234567") # חובה

class User(UserBase):
    id: int = Field(..., example=1)
    name: str = Field(..., example="John Doe")
    phone: str = Field(..., example="0501234567")
    # אין צורך בחשיפת hashed_password בסכמת התשובה

    class Config:
        from_attributes = True