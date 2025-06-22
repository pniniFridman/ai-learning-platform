// frontend/src/pages/RegisterPage.tsx
import { useState } from 'react';
import authService from '@/services/authService';
import { UserCreate } from '@/types/user';
import { useNavigate } from 'react-router-dom';

const RegisterPage: React.FC = () => {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [confirmPassword, setConfirmPassword] = useState<string>('');
  const [name, setName] = useState<string>(''); // החזרנו את השדה
  const [phone, setPhone] = useState<string>(''); // החזרנו את השדה
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError(null);
    setSuccess(null);

    if (password !== confirmPassword) {
      setError('Passwords do not match!');
      return;
    }

    try {
      // כעת שולחים את כל השדות הנדרשים: email, password, name, phone
      const userData: UserCreate = { email, password, name, phone };
      const newUser = await authService.registerUser(userData);

      setSuccess(`User ${newUser.email} registered successfully!`);
      // אפס את שדות הטופס לאחר רישום מוצלח
      setEmail('');
      setPassword('');
      setConfirmPassword('');
      setName('');
      setPhone('');

      // נווט לדף כניסה לאחר רישום מוצלח
      // הסרנו את ה-if ואת ה-setTimeout. הניווט יקרה מיד לאחר הצלחה.
      navigate('/login'); 
      
    } catch (err: any) {
      console.error("Registration error details (full error object):", err);

      let errorMessage = 'An unexpected error occurred during registration. Please try again.';

      if (err.response) {
        if (err.response.data && err.response.data.detail) {
          if (Array.isArray(err.response.data.detail)) {
            const messages = err.response.data.detail.map((detail: any) => {
              const field = detail.loc && detail.loc.length > 1 ? detail.loc[1] : 'Field';
              return `${field}: ${detail.msg}`;
            });
            errorMessage = messages.join('\n');
          } else if (typeof err.response.data.detail === 'string') {
            errorMessage = err.response.data.detail;
          } else {
            errorMessage = `Server Error: ${JSON.stringify(err.response.data.detail)}`;
          }
        } else if (typeof err.response.data === 'string') {
          errorMessage = err.response.data;
        } else {
          errorMessage = `Server Error: ${JSON.stringify(err.response.data)}`;
        }
      } else if (err.message) {
        errorMessage = `Network Error: ${err.message}`;
      }

      setError(errorMessage);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '400px', margin: '0 auto', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="email" style={{ display: 'block', marginBottom: '5px' }}>Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="name" style={{ display: 'block', marginBottom: '5px' }}>Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="phone" style={{ display: 'block', marginBottom: '5px' }}>Phone:</label>
          <input
            type="tel"
            id="phone"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            required
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="password" style={{ display: 'block', marginBottom: '5px' }}>Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            minLength={8}
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="confirmPassword" style={{ display: 'block', marginBottom: '5px' }}>Confirm Password:</label>
          <input
            type="password"
            id="confirmPassword"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            minLength={8}
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>
        {error && <p style={{ color: 'red', whiteSpace: 'pre-wrap' }}>{error}</p>}
        {success && <p style={{ color: 'green' }}>{success}</p>}
        <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>
          Register
        </button>
      </form>
    </div>
  );
};

export default RegisterPage;