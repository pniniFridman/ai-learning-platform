import React from 'react';
import { RouterProvider } from 'react-router-dom';
import router from './router'; // ייבוא ה-router שיצרנו

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;