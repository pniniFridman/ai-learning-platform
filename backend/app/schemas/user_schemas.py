from pydantic import BaseModel, Field
from typing import Optional

# Schema לבסיס המשתמש - שדות משותפים
class UserBase(BaseModel):
    name: str = Field(..., example="John Doe")
    phone: str = Field(..., example="0501234567")

# Schema ליצירת משתמש (כולל שדות שניתן להזין ביצירה)
class UserCreate(UserBase):
    pass # כרגע אין שדות נוספים מעבר ל-UserBase ביצירה

# Schema לתגובת API עבור משתמש (כולל שדה ה-ID שנוצר על ידי DB)
class User(UserBase):
    id: int = Field(..., example=1)

    class Config:
        from_attributes = True # או orm_mode = True בגרסאות Pydantic ישנות יותר
        # מאפשר ל-Pydantic לקרוא נתונים מאובייקטי ORM