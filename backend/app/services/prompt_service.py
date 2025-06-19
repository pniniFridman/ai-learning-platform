from sqlalchemy.orm import Session
from app.crud import prompt_crud, user_crud, category_crud, sub_category_crud
from app.schemas.prompt_schemas import PromptCreate
# נניח ש-AI_integration_service יהיה מודול נפרד
# from app.services.ai_integration_service import generate_lesson # אם יש כזה

def get_prompt_by_id(db: Session, prompt_id: int):
    """
    Service layer function to get a prompt by ID.
    """
    return prompt_crud.get_prompt(db, prompt_id)

def get_prompts_for_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    """
    Service layer function to get all prompts for a specific user.
    """
    return prompt_crud.get_prompts_by_user(db, user_id, skip=skip, limit=limit)

def create_new_prompt(db: Session, prompt: PromptCreate):
    """
    Service layer function to create a new prompt, including AI interaction.
    """
    # 1. ודא ש-user_id, category_id, sub_category_id קיימים
    user = user_crud.get_user(db, prompt.user_id)
    if not user:
        return None # User not found

    category = category_crud.get_category(db, prompt.category_id)
    if not category:
        return None # Category not found

    sub_category = sub_category_crud.get_sub_category(db, prompt.sub_category_id)
    if not sub_category:
        return None # SubCategory not found

    # 2. אינטגרציה עם AI (זהו מקום ללוגיקת AI)
    # response_from_ai = generate_lesson(prompt.prompt, category.name, sub_category.name)
    # כרגע נשתמש בתשובה המגיעה מה-prompt Create
    response_from_ai = prompt.response # זו הדמיה, במציאות זה יגיע מ-AI

    # 3. יצירת האובייקט prompt ב-DB
    db_prompt = prompt_crud.create_prompt(db=db, prompt=prompt)
    if db_prompt:
        # אם ה-AI_integration_service היה מחזיר תשובה, היינו מעדכנים אותה כאן
        # db_prompt.response = response_from_ai
        db.commit() # לוודא שהשינויים נשמרו לאחר עדכון השדה response
        db.refresh(db_prompt)
    return db_prompt