# Task Manager Backend

A RESTful Task Manager API built using **Python, FastAPI, and SQLite**. This application allows users to create, view, update, delete, and filter tasks through API endpoints.

## Features

- Create new tasks.
- Retrieve all tasks.
- Retrieve a task by its ID.
- Update existing tasks.
- Delete tasks.
- Mark tasks as completed or pending.
- Filter tasks by completion status.
- SQLite database integration.
- API documentation with Swagger UI.
- Error handling for invalid requests and missing tasks.

## Technologies Used

- **Python** – Programming language
- **FastAPI** – Backend web framework
- **SQLite** – Database
- **SQLAlchemy** – ORM
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server

## Project Structure

```text
Task_manager/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   └── routers/
│       ├── __init__.py
│       └── tasks.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/tarunkumarmtk12-droid/Task_manager-backend.git
```

### 2. Navigate to the project

```bash
cd Task_manager-backend
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

The application will run at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI automatically generates interactive API documentation.

**Swagger UI:**

`http://127.0.0.1:8000/docs`

**ReDoc:**

`http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/tasks/` | Create a task |
| GET | `/api/tasks/` | Get all tasks |
| GET | `/api/tasks/{task_id}` | Get task by ID |
| PUT | `/api/tasks/{task_id}` | Update a task |
| DELETE | `/api/tasks/{task_id}` | Delete a task |
| GET | `/api/tasks/filter/?completed=true` | Filter completed or pending tasks |

## Database

The application uses SQLite with SQLAlchemy ORM to store and manage task information.

Database file: `tasks.db`

## Future Improvements

- User authentication and authorization.
- Task deadlines and reminders.
- Task priority management.
- Frontend integration.
- Deployment to a cloud platform.

## Author

**Tarun**

Python Backend Developer

---

*This project was developed to demonstrate REST API development, database integration, CRUD operations, and backend application development using Python and FastAPI.*