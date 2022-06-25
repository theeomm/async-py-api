from typing import Optional

from sqlmodel import Field, SQLModel


class TodoModel(SQLModel):
    note: str
    created_at: str


class Todo(TodoModel, table=True):
    __tablename__ = "todos"
    id: Optional[int] = Field(default=None, primary_key=True)


class TodoCreate(TodoModel):
    pass


class TodoUpdate(TodoModel):
    note: Optional[str] = None
