from fastapi import FastAPI
from app.routers import auth, task
from app.database.database import engine, Base

app = FastAPI(title="Task Management API")

# Register our routers
app.include_router(auth.router)
app.include_router(task.router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Management API"}
