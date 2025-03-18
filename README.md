# FastAPI Task Manager with Authentication

This is a **FastAPI**-based Task Manager application with user authentication (JWT-based) and email confirmation. 🚀

## Features

- ✅ User Registration with Email Confirmation 📧
- ✅ Secure User Authentication with JWT 🔐
- ✅ CRUD Operations for Todo Tasks ✅
- ✅ User-specific Task Management 📝
- ✅ FastAPI + PostgreSQL Integration⚡

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/fastapi-todo-app.git
   cd fastapi-todo-app
   ```

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (e.g., `.env` file)

5. **Run the application**

   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/v1/user/register` | Register a new user |
| `POST` | `/api/v1/user/login` | Login user and get JWT |
| `GET`  | `/api/v1/user/confirm-email/{token}` | Confirm user email |

### Todo Management

| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/api/v1/task/check-task` | Retrieve all tasks |
| `POST` | `/api/v1/task/create-task` | Create a new task |
| `PUT`  | `/api/v1/task/update-task/{task_id}` | Update a task |
| `DELETE` | `/api/v1/task/delete-task/{task_id}` | Delete a task |

## Example Usage

1. **Register a user**

   ```json
   {
     "first_name": "John",
     "last_name": "Doe",
     "email": "john@example.com",
     "password": "securepassword"
   }
   ```

2. **Login to get a token**

   ```json
   {
     "email": "john@example.com",
     "password": "securepassword"
   }
   ```

   Response:

   ```json
   {
     "token": "Bearer your_jwt_token_here"
   }
   ```

3. **Use the token to access protected routes**

   ```bash
   curl -H "Authorization: Bearer your_jwt_token_here" http://127.0.0.1:8000/api/v1/check-task
   ```

## License

This project is licensed under the **MIT License**.

---

Made with ❤️ by Elijah 🚀
