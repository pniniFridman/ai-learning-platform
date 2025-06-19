from pydantic import BaseModel, Field
from typing import Optional
# אם נרצה לכלול את Category בתוך SubCategory, נצטרך את זה:
# from __future__ import annotations # מאפשר forward references

# Schema לבסיס תת-הקטגוריה
class SubCategoryBase(BaseModel):
    name: str = Field(..., example="Space")
    category_id: int = Field(..., example=1)

# Schema ליצירת תת-קטגוריה
class SubCategoryCreate(SubCategoryBase):
    pass

# Schema לתגובת API עבור תת-קטגוריה
class SubCategory(SubCategoryBase):
    id: int = Field(..., example=1)
    # כדי לכלול את אובייקט הקטגוריה המשויכת, תצטרכי להוסיף:
    # category: Category # ולוודא ייבוא נכון של Category
    # נטפל בזה בהמשך במידת הצורך

    class Config:
        from_attributes = True