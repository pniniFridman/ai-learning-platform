from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Schema לבסיס הפרומפט
class PromptBase(BaseModel):
    user_id: int = Field(..., example=1)
    category_id: int = Field(..., example=1)
    sub_category_id: int = Field(..., example=1)
    prompt: str = Field(..., example="Teach me about black holes.")
    response: str = Field(..., example="A black hole is a region of spacetime where gravity is so strong...")

# Schema ליצירת פרומפט
class PromptCreate(PromptBase):
    pass

# Schema לתגובת API עבור פרומפט
class Prompt(PromptBase):
    id: int = Field(..., example=1)
    created_at: datetime = Field(..., example=datetime.now())

    class Config:
        from_attributes = True