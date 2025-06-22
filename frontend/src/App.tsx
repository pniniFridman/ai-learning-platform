// App.tsx
import { RouterProvider } from 'react-router-dom'; // ודא שרק RouterProvider מיובא
import router from '@/router'; // ייבוא ה-router שיצרת בקובץ router/index.tsx

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;