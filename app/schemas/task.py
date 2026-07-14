from pydantic import BaseModel

# Base model contains fields that are common to create/update/response
class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str | None = "todo"
    deadline: str | None = None

# We inherit from TaskBase for creating a task
class TaskCreate(TaskBase):
    pass

# For updates, all fields are optional because the user might just want to update one field
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    deadline: str | None = None

# The response includes everything in TaskBase plus id and owner_id
class TaskResponse(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
