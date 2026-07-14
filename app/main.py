from fastapi import FastAPI
from app.routers import auth, task
from app.database.database import engine, Base

# This line creates the tables in our database automatically 
# (useful for learning, though normally we'd use Alembic migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

# Register our routers
app.include_router(auth.router)
app.include_router(task.router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Management API"}
