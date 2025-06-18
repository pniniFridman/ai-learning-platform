from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, text 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    POSTGRES_USER = os.getenv("POSTGRES_USER", "user")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "learning_platform_db")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():

    db = SessionLocal()
    try:

        yield db
    finally:
        db.close()
  
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    description = Column(String)
    instructor = Column(String)

def create_db_tables():
    
    Base.metadata.create_all(bind=engine)
   
app = FastAPI(
    on_startup=[create_db_tables]
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Learning Platform Backend!"}

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):

    db_connected = False
    try:

        db.execute(text("SELECT 1")) 
        db_connected = True

    except Exception as e:
        db_connected = False
        
    finally:
       
    return {"status": "ok", "db_connected": db_connected}

class CourseBase(BaseModel):
    title: str
    description: str
    instructor: str

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True

@app.post("/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):

    db_course = Course(title=course.title, description=course.description, instructor=course.instructor)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course

@app.get("/courses/", response_model=list[CourseResponse])
async def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    courses = db.query(Course).offset(skip).limit(limit).all()

    return courses

@app.get("/courses/{course_id}", response_model=CourseResponse)
async def read_course(course_id: int, db: Session = Depends(get_db)):

    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    return course

@app.put("/courses/{course_id}", response_model=CourseResponse)
async def update_course(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):

    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    db_course.title = course.title
    db_course.description = course.description
    db_course.instructor = course.instructor

    db.commit()
    db.refresh(db_course)

    return db_course

@app.delete("/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int, db: Session = Depends(get_db)):

    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    db.delete(db_course)
    db.commit()
    
    return