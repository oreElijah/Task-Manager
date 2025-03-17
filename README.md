# FastAPI Task Management API

## Overview
This is a Task Management API built using **FastAPI** with **PostgreSQL** as the database. It provides user authentication and CRUD operations for managing tasks.

## Features
- **User Authentication**: Secure authentication using JWT tokens.
- **Task Management**: Users can create, retrieve, update, and delete tasks.
- **FastAPI**: High-performance framework for building APIs with automatic documentation.
- **PostgreSQL**: Robust and scalable relational database for storing tasks.
- **No ORM**: Direct SQL queries are used instead of an ORM.

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL
- Virtual Environment (optional but recommended)

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/fastapi-task-api.git
   cd fastapi-task-api
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the project root with the following variables:
   ```ini
   DATABASE_URL=postgresql://user:password@localhost/dbname
   SECRET_KEY=your_secret_key_here
   ```

5. **Start the Server**
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Authentication
- `POST /register/` - Register a new user
- `POST /login/` - Log in to get an access token

### Tasks
- `POST /task/` - Create a new task (Authenticated)
- `GET /tasks/` - Retrieve all tasks (Authenticated)
- `PUT /task/{task_id}` - Update a task (Authenticated)
- `DELETE /task/{task_id}` - Delete a task (Authenticated)

## Documentation
Once the server is running, access the interactive API documentation at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
