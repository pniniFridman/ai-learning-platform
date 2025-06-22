# AI Learning Platform

Welcome to the AI Learning Platform! This project provides a full-stack web application designed to facilitate AI-powered learning by allowing users to submit prompts, view AI-generated responses, and track their learning history. It also includes an administration dashboard for managing users and their activities.

## Features

This platform includes the following key features:

### Backend
* **User Management**: Supports registration and management of user accounts.
    * Secure password hashing (using `bcrypt`).
    * Prevention of duplicate email and phone number registrations.
* **Prompt/Learning History**: Stores and manages user-submitted prompts and AI-generated responses.
* **Database**: Utilizes PostgreSQL for robust data storage.
* **API**: Provides RESTful APIs for frontend communication.

### Frontend
* **User Registration**: Allows new users to create an account.
* **User Login**: Enables existing users to sign in. (Note: Automatic login after registration is planned/implemented for improved UX).
* **Main Dashboard**: For regular users to select categories, submit prompts, and view AI responses.
* **Learning History**: Dedicated page to view a user's past prompts and AI responses.
* **Admin Dashboard**: A privileged area to list all users and review their prompt history.
* **Error Handling**: Includes a 404 Not Found page for invalid routes.

## Technologies Used

### Backend
* **Python**: Primary programming language.
* **FastAPI**: Web framework for building APIs.
* **SQLAlchemy**: ORM (Object Relational Mapper) for database interactions.
* **PostgreSQL**: Relational database.
* **Uvicorn**: ASGI server for running the FastAPI application.
* **Bcrypt**: For secure password hashing.

### Frontend
* **React**: JavaScript library for building user interfaces.
* **TypeScript**: Superset of JavaScript for type-safe code.
* **React Router DOM**: For client-side routing.
* **Vite**: Fast build tool for modern web projects.
* **Axios**: HTTP client for making API requests.

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

* Python 3.8+
* Node.js (LTS recommended)
* npm or Yarn (for frontend dependencies)
* PostgreSQL database server installed and running.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/pniniFridman/ai-learning-platform.git](https://github.com/pniniFridman/ai-learning-platform.git)
    cd ai-learning-platform
    ```

2.  **Backend Setup:**
    Navigate into the `backend` directory, create a virtual environment, install dependencies, and set up the database.

    ```bash
    cd backend
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate # On macOS/Linux
    pip install -r requirements.txt
    ```
    * **Database Configuration**:
        Ensure your PostgreSQL database is running. You will likely need to configure your database connection string in a `.env` file or similar mechanism (e.g., `DATABASE_URL=postgresql://user:password@host:port/dbname`).
        _Note: Based on previous interactions, `postgresql://postgres:your_postgres_password@localhost/postgres` was used for local setup._

3.  **Frontend Setup:**
    Open a new terminal, navigate into the `frontend` directory, and install dependencies.

    ```bash
    cd frontend
    npm install # or yarn install
    ```

### Running the Application

1.  **Start the Backend Server:**
    From the `backend` directory (with your virtual environment activated):
    ```bash
    uvicorn app.main:app --reload
    ```
    The backend API will be available at `http://172.0.0.1:8000`.

2.  **Start the Frontend Development Server:**
    From the `frontend` directory (in a separate terminal):
    ```bash
    npm run dev # or yarn dev
    ```
    _Note: For Vite projects, the typical command to start the development server is `npm run dev` or `yarn dev`, not `npm start`._
    The frontend application will be available at `http://localhost:5173`.

## Project Structure

ai-learning-platform/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoints/ (user_api.py, etc.)
│   │   ├── core/ (security.py, etc.)
│   │   ├── database/ (database.py)
│   │   ├── models/ (user_model.py, etc.)
│   │   ├── schemas/ (user_schemas.py, auth_schemas.py, etc.)
│   │   └── services/ (user_service.py, auth_service.py, etc.)
│   ├── tests/
│   ├── venv/
│   ├── .env.example
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/ (HomePage.tsx, RegisterPage.tsx, LoginPage.tsx, DashboardPage.tsx, etc.)
│   │   ├── router/ (index.tsx)
│   │   ├── services/ (authService.ts, api.ts, etc.)
│   │   ├── types/ (user.d.ts)
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── .env.example
│   ├── index.html
│   ├── package.json
│   └── tsconfig.json
└── README.md


## Future Enhancements

These are the features that are planned for future development to complete the project:

* **Implement automatic login after user registration**: To improve user experience, automatically log in the user after successful registration, eliminating the need to visit the login page immediately.
* **Implement user login functionality**: Enable existing users to securely log in to their accounts using their credentials.
* **Backend: Implement robust token-based authentication**: Secure the API using JWT (JSON Web Tokens) for authentication and authorization across all protected endpoints.
* **Frontend: Securely store JWT token**: Implement mechanisms to securely store and manage the JWT token in the frontend (e.g., localStorage, Context API, or Redux Toolkit) after successful login/registration.
* **Frontend & Backend: Implement authentication flow for protected routes**: Ensure that only authenticated users can access specific pages and API endpoints.
* **Backend: Create API endpoints for prompt submission and retrieval**: Implement the necessary backend logic for users to submit AI prompts (including category and sub-category selection) and retrieve the AI-generated responses.
* **Frontend: Implement prompt submission form**: Develop the user interface for submitting prompts to the AI, including input fields for text and selection for categories/sub-categories.
* **Frontend: Display AI-generated responses**: Implement the UI to clearly display the responses received from the AI model.
* **Backend: Implement API endpoints for learning history**: Develop backend functionality to store and retrieve a comprehensive history of a user's submitted prompts and the corresponding AI responses.
* **Frontend: Implement learning history page**: Create a dedicated page for users to view and manage their personal learning history.
* **Backend: Implement API endpoints for admin dashboard**: Develop backend endpoints that allow administrators to list all users, view their details, and access their complete prompt history.
* **Frontend: Implement admin dashboard page**: Build the user interface for the admin dashboard, providing functionalities for user management and viewing all prompt histories.
* **Integrate with an AI model**: (This is a core feature but implies connection to an external AI service, which will be needed for prompt generation).