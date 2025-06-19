from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text # נשמור את זה אם נשתמש ב-health_check בקובץ זה
# ייבוא תלויות ממבנה התיקיות החדש
from .database.database import engine, Base, get_db
from .models import course as models_course # ייבוא מודל הקורס כדי לוודא ש-Base.metadata רואה אותו
from .api.endpoints import course as course_api # ייבוא ה-router של הקורסים
# ייבוא המודלים החדשים כדי ש-SQLAlchemy יכיר אותם ויצור טבלאות עבורם
# חשוב שהייבוא יתבצע לפני קריאה ל-Base.metadata.create_all()
from app.models.User import User
from app.models.Category import Category
from app.models.SubCategory import SubCategory
from app.models.Prompt import Prompt

# פונקציה ליצירת טבלאות

def create_db_tables():
    print("Creating database tables...")
    # ודא שכל המודלים שיובאו והוגדרו כ-Base, אכן ייווצרו
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

# הגדרת lifespan לטיפול באירועי startup ו-shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # קוד שירוץ עם עליית היישום (startup)
    create_db_tables()
    yield
    # קוד שירוץ עם כיבוי היישום (shutdown)
    print("Application shutdown event.")

# יצירת מופע FastAPI עם lifespan
app = FastAPI(lifespan=lifespan) # שינוי כאן: העבר את lifespan לתוך FastAPI

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
        pass # הסרנו את ה-print, אין צורך ב-finally אם אין פעולה נוספת
    return {"status": "ok", "db_connected": db_connected}
