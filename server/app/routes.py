from typing import Union

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import schemas, controller
from .dependencies import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["v1"],
    responses={404: {"description": "Not found"}},
)

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = controller.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return controller.create_user(db=db, user=user)


@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = controller.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = controller.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/records/", response_model=schemas.Record)
def create_record_for_user(
    user_id: int, record: schemas.RecordCreate, db: Session = Depends(get_db)
):
    return controller.create_user_record(db=db, record=record, user_id=user_id)


@router.get("/records/", response_model=list[schemas.Record])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = controller.get_records(db, skip=skip, limit=limit)
    return records


@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}