from sqlalchemy.orm import Session
from app.crud import course_crud # ייבוא פונקציות ה-CRUD עבור קורסים
from app.schemas.course_schemas import CourseCreate # ייבוא סכמת יצירת קורס

def get_course_by_id(db: Session, course_id: int):
    """
    Service layer function to get a course by ID.
    """
    return course_crud.get_course(db, course_id)

def get_all_courses(db: Session, skip: int = 0, limit: int = 100):
    """
    Service layer function to get all courses.
    """
    return course_crud.get_courses(db, skip=skip, limit=limit)

def create_new_course(db: Session, course: CourseCreate):
    """
    Service layer function to create a new course.
    Includes business logic like checking for existing course title.
    """
    db_course = course_crud.get_course_by_title(db, title=course.title)
    if db_course:
        return None # Course with this title already exists
    return course_crud.create_course(db=db, course=course)