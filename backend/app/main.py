from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text # נשמור את זה אם נשתמש ב-health_check בקובץ זה

# ייבוא תלויות ממבנה התיקיות החדש
from .database.database import engine, Base, get_db
from .models import course as models_course # ייבוא מודל הקורס כדי לוודא ש-Base.metadata רואה אותו
from .api.endpoints import course as course_api # ייבוא ה-router של הקורסים

# פונקציה ליצירת טבלאות
def create_db_tables():
    print("Creating database tables...")
    # לוודא שכל המודלים מיובאים לפני create_all
    # במקרה זה, models_course כבר יובא למעלה
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

app = FastAPI(
    on_startup=[create_db_tables]
)

# הוספת ה-router של הקורסים לאפליקציה הראשית
app.include_router(course_api.router)

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
        # ניתן להוסיף לוגינג כאן במקום print
    finally:
        pass # הסרנו את ה-print, אין צורך ב-finally אם אין פעולה נוספת
    return {"status": "ok", "db_connected": db_connected}