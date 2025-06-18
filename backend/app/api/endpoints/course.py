from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text # נשאיר את זה זמנית, נחליט אם למחוק בהמשך

# ייבוא מהמודולים החדשים שיצרנו
from ...database.database import get_db, Base, engine # ייבוא Base ו-engine
from ...schemas import course as schemas_course # ייבוא ישיר של הסכימות מקובץ course
from ...models import course as models_course # ייבוא מודל הקורס

# ניתן ליצור פונקציות CRUD כאן או בתיקיית crud
# נתחיל לשים את הלוגיקה כאן, ואז נשקול להעביר ל-crud אם תרצה/י

router = APIRouter(
    prefix="/courses", # הגדרת קידומת לכל ה-endpoints ב-router הזה
    tags=["courses"],  # תיוג עבור ה-Swagger UI
)

@router.post("/", response_model=schemas_course.CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(course: schemas_course.CourseCreate, db: Session = Depends(get_db)):
    db_course = models_course.Course(title=course.title, description=course.description, instructor=course.instructor)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/", response_model=list[schemas_course.CourseResponse])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = db.query(models_course.Course).offset(skip).limit(limit).all()
    return courses

@router.get("/{course_id}", response_model=schemas_course.CourseResponse)
def read_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models_course.Course).filter(models_course.Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=schemas_course.CourseResponse)
def update_course(course_id: int, course: schemas_course.CourseCreate, db: Session = Depends(get_db)):
    db_course = db.query(models_course.Course).filter(models_course.Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    db_course.title = course.title
    db_course.description = course.description
    db_course.instructor = course.instructor

    db.commit()
    db.refresh(db_course)
    return db_course

@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(models_course.Course).filter(models_course.Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    db.delete(db_course)
    db.commit()
    return # No content for 204 status