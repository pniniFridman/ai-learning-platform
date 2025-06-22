// frontend/src/services/authService.ts
import api from '@/services/api'; // ייבוא האובייקט axios שהגדרנו
import { UserCreate, User, Token } from '@/types/user'; // ייבוא הטיפוסים שיצרנו

const authService = {
  /**
   * שולח בקשה לרישום משתמש חדש.
   * @param userData נתוני המשתמש (מייל וסיסמה).
   * @returns Promise עם אובייקט המשתמש שנוצר.
   */
  registerUser: async (userData: UserCreate): Promise<User> => {
    try {
      const response = await api.post<User>('/users/', userData); // נתיב ה-API לרישום משתמשים
      return response.data;
    } catch (error) {
      console.error('Registration failed:', error);
      throw error; // זרוק את השגיאה הלאה לטיפול בקומפוננטה
    }
  },

  /**
   * שולח בקשה להתחברות משתמש וקבלת טוקן.
   * @param email מייל המשתמש.
   * @param password סיסמת המשתמש.
   * @returns Promise עם אובייקט הטוקן.
   */
  loginUser: async (email: string, password: string): Promise<Token> => {
    try {
      // Axios מצפה לנתוני Form Data עבור בקשות application/x-www-form-urlencoded
      // FastAPI משתמש בזה עבור OAuth2 password flow
      const formData = new URLSearchParams();
      formData.append('username', email); // ב-FastAPI, השדה הוא 'username' עבור מייל
      formData.append('password', password);

      const response = await api.post<Token>('/token', formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });
      // שמירת הטוקן ב-localStorage
      localStorage.setItem('accessToken', response.data.access_token);
      localStorage.setItem('tokenType', response.data.token_type);
      return response.data;
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  },

  /**
   * פונקציה להתנתקות (ניקוי הטוקן).
   */
  logout: () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('tokenType');
    // ניתן להוסיף כאן ניקוי של מצב (state) גלובלי אם יש כזה
  },
};

export default authService;