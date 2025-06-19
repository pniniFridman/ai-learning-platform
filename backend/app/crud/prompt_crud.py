from sqlalchemy.orm import Session
from app.models.Prompt import Prompt # ודאי שהייבוא נכון
from app.schemas.prompt_schemas import PromptCreate # ודאי שהייבוא נכון

def get_prompt(db: Session, prompt_id: int):
    """
    Retrieves a prompt by ID.
    """
    return db.query(Prompt).filter(Prompt.id == prompt_id).first()

def get_prompts_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    """
    Retrieves prompts for a specific user.
    """
    return db.query(Prompt).filter(Prompt.user_id == user_id).offset(skip).limit(limit).all()

def create_prompt(db: Session, prompt: PromptCreate):
    """
    Creates a new prompt record in the database.
    """
    db_prompt = Prompt(
        user_id=prompt.user_id,
        category_id=prompt.category_id,
        sub_category_id=prompt.sub_category_id,
        prompt=prompt.prompt,
        response=prompt.response
    )
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt