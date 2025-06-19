from pydantic import BaseModel, Field
from typing import Optional, List
# אם נרצה לכלול את SubCategory בתוך Category, נצטרך את זה:
# from __future__ import annotations # מאפשר forward references

# Schema לבסיס הקטגוריה
class CategoryBase(BaseModel):
    name: str = Field(..., example="Science")

# Schema ליצירת קטגוריה
class CategoryCreate(CategoryBase):
    pass

# Schema לתגובת API עבור קטגוריה
class Category(CategoryBase):
    id: int = Field(..., example=1)
    # כדי לכלול רשימה של תתי-קטגוריות משויכות, תצטרכי להוסיף:
    # sub_categories: List[SubCategory] = [] # ולוודא ייבוא נכון של SubCategory
    # נטפל בזה בהמשך במידת הצורך

    class Config:
        from_attributes = True