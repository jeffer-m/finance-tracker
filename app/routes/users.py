from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select, Session
from app.models.users import User, UserCreate
from app.services.db import get_session
from uuid6 import uuid7

usersRouter = APIRouter(
    prefix="/users",
    tags=["users"],
)

def check_user_exists(session: Session, email=None, username=None):
    if email:
        if session.exec(select(User).where(User.email == email)).first():
            return "Email already registered"
    
    if username:
        if session.exec(select(User).where(User.username == username)).first():
            return "Username already taken"
    
    return None

@usersRouter.get("/{user_id}")
def get_users(user_id, session: Session = Depends(get_session)) -> User:
   user = session.exec(select(User).where(User.id == user_id)).first()
   
   return user

@usersRouter.post("/create")
def create_user(user: UserCreate, session: Session = Depends(get_session)) -> User:
    
    error = check_user_exists(session, email=user.email, username=user.username)
    if error:
        raise HTTPException(status_code=400, detail=error)
    
    new_user = User(id=uuid7(), **user.model_dump())
    
    session.add(new_user)
    
    session.commit()
    
    session.refresh(new_user)
    
    return new_user
    