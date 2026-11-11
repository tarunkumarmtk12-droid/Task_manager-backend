from fastapi import FastAPI

from app.database import Base, engine
from app.routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="Backend REST API for Task Management",
    version="1.0.0"
)


app.include_router(tasks.router)


@app.get("/")
def home():

    return {
        "message": "Task Manager API is running"
    }