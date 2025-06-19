from sqlalchemy.orm import Session
from app.models.Course import Course # ייבוא נכון של מודל Course
from app.schemas.course_schemas import CourseCreate # ייבוא נכון של סכמת CourseCreate

def get_course(db: Session, course_id: int):
    """
    Retrieves a course by ID.
    """
    return db.query(Course).filter(Course.id == course_id).first()

def get_course_by_title(db: Session, title: str):
    """
    Retrieves a course by its title.
    """
    return db.query(Course).filter(Course.title == title).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieves a list of courses.
    """
    return db.query(Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: CourseCreate):
    """
    Creates a new course in the database.
    """
    db_course = Course(
        title=course.title,
        description=course.description,
        instructor=course.instructor
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# פונקציות לעדכון ומחיקה (אפשר להוסיף בעתיד לפי הצורך)
# def update_course(db: Session, course_id: int, course_update: CourseCreate):
#     db_course = db.query(Course).filter(Course.id == course_id).first()
#     if db_course:
#         for key, value in course_update.model_dump(exclude_unset=True).items():
#             setattr(db_course, key, value)
#         db.commit()
#         db.refresh(db_course)
#     return db_course

# def delete_course(db: Session, course_id: int):
#     db_course = db.query(Course).filter(Course.id == course_id).first()
#     if db_course:
#         db.delete(db_course)
#         db.commit()
#     return db_course