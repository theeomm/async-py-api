from fastapi import Depends, Query
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from sqlmodel import Session, select

from app.models.todo import Todo, TodoCreate, TodoUpdate
from app.utils import get_session

router = APIRouter(prefix="/todos")


@router.get("/", response_model=list[Todo])
async def index(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=10, lte=100),
):
    """
    Returns a list of todos
    """
    query = select(Todo).limit(limit).offset(offset)
    todos: list[Todo] = session.exec(query).all()

    return todos


@router.post("/", response_model=Todo)
async def new(
    *,
    session: Session = Depends(get_session),
    data: TodoCreate,
):
    """
    Add a new Todo
    """
    todo = Todo.from_orm(data)
    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


@router.get("/{id}", response_model=Todo)
async def todo(
    *,
    session: Session = Depends(get_session),
    id: int,
):
    """
    Retrieve a single todo
    """

    todo: Todo = session.get(Todo, id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


@router.patch("/{id}", response_model=Todo)
async def update(
    *,
    session: Session = Depends(get_session),
    id: int,
    data: TodoUpdate,
):
    """
    Update a todo
    """
    todo: Todo = session.get(Todo, id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo_data = data.dict(exclude_unset=True)

    for key, val in todo_data.items():
        setattr(todo, key, val)

    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


@router.delete("/{id}", response_model=Todo)
async def delete(
    *,
    session: Session = Depends(get_session),
    id: int,
):
    todo: Todo = session.get(Todo, id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    session.delete(todo)
    session.commit()

    return todo
