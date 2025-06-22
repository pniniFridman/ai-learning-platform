// frontend/src/types/user.d.ts

// ממשק עבור יצירת משתמש (מה שה-Frontend ישלח ל-Backend)
export interface UserCreate {
  email: string;
  password: string;
  is_admin?: boolean; // אם אפשר ליצור משתמש אדמין דרך ההרשמה
  name: string; // הוסף שדה שם
  phone: string;
}

// ממשק עבור תגובת המשתמש מה-Backend (מה שה-Backend יחזיר)
export interface User {
  id: number;
  email: string;
  name: string;
  phone: string;
  is_active: boolean;
  is_admin: boolean;
  // ניתן להוסיף כאן שדות נוספים אם ה-Backend מחזיר אותם (לדוגמה, created_at)
}

// ממשק עבור תגובת טוקן מה-Backend (לדוגמה, לאחר התחברות)
export interface Token {
  access_token: string;
  token_type: string;
}