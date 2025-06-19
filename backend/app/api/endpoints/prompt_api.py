from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.prompt_schemas import Prompt, PromptCreate
from app.services import prompt_service
from app.database.database import get_db

router = APIRouter(prefix="/prompts", tags=["Prompts"])

@router.post("/", response_model=Prompt, status_code=status.HTTP_201_CREATED)
def create_prompt_endpoint(prompt: PromptCreate, db: Session = Depends(get_db)):
    """
    Create a new prompt and get an AI-generated response.
    """
    db_prompt = prompt_service.create_new_prompt(db=db, prompt=prompt)
    if db_prompt is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create prompt. Check if user, category, or sub-category exist."
        )
    return db_prompt

@router.get("/", response_model=List[Prompt])
def read_prompts_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all prompts.
    """
    prompts = prompt_service.get_all_prompts(db, skip=skip, limit=limit) # Note: this function doesn't exist yet, adjust later if needed
    # For now, let's just return all prompts, or specifically prompts by user as it's more relevant
    # The prompt_service only has get_prompts_for_user currently
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Get all prompts not implemented yet. Use /prompts/by-user/{user_id} instead.")

@router.get("/by-user/{user_id}", response_model=List[Prompt])
def read_prompts_by_user_endpoint(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve prompts filtered by a specific user ID (learning history).
    """
    prompts = prompt_service.get_prompts_for_user(db, user_id=user_id, skip=skip, limit=limit)
    return prompts

@router.get("/{prompt_id}", response_model=Prompt)
def read_prompt_endpoint(prompt_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single prompt by ID.
    """
    prompt = prompt_service.get_prompt_by_id(db, prompt_id=prompt_id)
    if prompt is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prompt not found")
    return prompt