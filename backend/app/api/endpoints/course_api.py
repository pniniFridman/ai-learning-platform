from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.course_schemas import CourseCreate, CourseResponse
from app.services import course_service
from app.database.database import get_db
# הקוד המקורי שלך כנראה ייבא את המודל, אם אין בו צורך ב-router עצמו, ניתן להסירו
# from app.models.Course import Course as models_course # זה היה שם הייבוא שלך בעבר

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course_endpoint(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course.
    """
    db_course = course_service.create_new_course(db=db, course=course)
    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Course with this title already exists"
        )
    return db_course

@router.get("/", response_model=List[CourseResponse])
def read_courses_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all courses.
    """
    courses = course_service.get_all_courses(db, skip=skip, limit=limit)
    return courses

@router.get("/{course_id}", response_model=CourseResponse)
def read_course_endpoint(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single course by ID.
    """
    course = course_service.get_course_by_id(db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course