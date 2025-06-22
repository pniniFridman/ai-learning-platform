# main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List

# הוסף את ייבוא ה-CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware 

# ייבוא הגדרות מסד הנתונים
from app.database.database import engine, Base, get_db

# ייבוא כל המודלים (הטבלאות) כדי ש-SQLAlchemy יכיר אותם ויוכל ליצור עבורם טבלאות
# חשוב לוודא ששמות הקבצים והמחלקות תואמים לייבוא
from app.models.User import User
from app.models.Category import Category
from app.models.SubCategory import SubCategory
from app.models.Prompt import Prompt
from app.models.Course import Course # ודא ששם הקובץ הוא Course.py והמחלקה היא Course

# ייבוא ה-routers של ה-API מתיקיית endpoints
from app.api.endpoints import user_api
from app.api.endpoints import category_api
from app.api.endpoints import sub_category_api
from app.api.endpoints import prompt_api
from app.api.endpoints import course_api

# פונקציה ליצירת טבלאות במסד הנתונים בעת הפעלת האפליקציה
def create_db_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

# פונקציית lifespan לטיפול באירועי startup/shutdown של האפליקציה
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles startup and shutdown events for the application.
    Used for initializing database tables.
    """
    create_db_tables()
    yield
    print("Application shutdown.")

# הגדרת אפליקציית FastAPI (הגדרה יחידה ונכונה)
app = FastAPI(
    title="AI Learning Platform API",
    description="API for managing users, categories, prompts, and courses in an AI-powered learning platform.",
    version="0.1.0",
    lifespan=lifespan # קשור את פונקציית ה-lifespan לאפליקציה
)

# הגדרות CORS - בלוק זה חייב להיות כאן, אחרי הגדרת ה-app
origins = [
    "http://localhost:5173",  # הכתובת של ה-Frontend שלך
    "http://127.0.0.1:5173",  # ודא שגם זה כלול ליתר ביטחון
    # הוסף כאן כל כתובת נוספת שה-Frontend יכול לרוץ עליה
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # מאפשר את כל המתודות (GET, POST, PUT, DELETE, OPTIONS וכו')
    allow_headers=["*"],  # מאפשר את כל הכותרות בבקשה
)


# כלול את ה-routers של ה-API
# כל router מוסיף קבוצה של endpoints תחת prefix מסוים
app.include_router(user_api.router)
app.include_router(category_api.router)
app.include_router(sub_category_api.router)
app.include_router(prompt_api.router)
app.include_router(course_api.router)

# דוגמאות ל-endpoints בסיסיים
@app.get("/", summary="Root endpoint", tags=["Root"])
async def read_root():
    """
    Welcome message for the AI Learning Platform Backend.
    """
    return {"message": "Welcome to the AI Learning Platform Backend!"}

@app.get("/health", summary="Health Check", tags=["Monitoring"])
async def health_check(db: Session = Depends(get_db)):
    """
    Checks the health of the application and database connection.
    """
    db_connected = False
    try:
        db.execute(text("SELECT 1"))
        db_connected = True
    except Exception as e:
        print(f"Database connection error: {e}")
        db_connected = False
    finally:
        pass # The get_db dependency handles closing the session automatically

    return {"status": "ok", "db_connected": db_connected}

