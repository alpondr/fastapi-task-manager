# Task Management API

This is a backend API project I built to learn FastAPI and PostgreSQL. It is a simple task management system where users can register, login, and manage their own tasks.

## Features

- User registration and login using JWT authentication
- Create, read, update, and delete tasks
- Users can only see and edit their own tasks
- Task list has basic pagination and status filtering

## Tech Stack

- Python 3.11+
- FastAPI
- PostgreSQL & SQLAlchemy
- Pydantic for data validation
- python-jose and passlib for security

## How to run locally

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy the `.env.example` file and rename it to `.env`. Update your PostgreSQL database URL in this file.

4. Run the API:
   ```bash
   fastapi dev app/main.py
   ```
   *(Alternatively, you can run `uvicorn app.main:app --reload`)*

5. Go to `http://127.0.0.1:8000/docs` in your browser to see the interactive API documentation and test the endpoints.
