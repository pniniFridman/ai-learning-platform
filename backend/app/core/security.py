# backend/app/core/security.py
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
import os

# הגדרת אלגוריתם ה-hashing לסיסמאות
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# הגדרות JWT
# חשוב: SECRET_KEY צריך לבוא ממשתנה סביבה בסביבת ייצור (production)
# לצורך פיתוח, אפשר לשים כאן ערך, אבל שנה אותו בהמשך.
SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key-for-development") # שנה את זה למפתח סודי חזק וייחודי!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # זמן תפוגה לטוקן גישה

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """מאמת סיסמה פשוטה מול סיסמה מוצפנת."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """מצפין סיסמה פשוטה."""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """יוצר טוקן גישה (JWT)."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    """מאמת טוקן (JWT) ומחזיר את שם המשתמש (sub)."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception