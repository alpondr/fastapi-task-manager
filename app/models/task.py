from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="todo") # options: todo, in_progress, done
    deadline = Column(String, nullable=True)
    
    # The foreign key that links this task to a specific user
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Establishing relationship with the User model
    owner = relationship("User", back_populates="tasks")
