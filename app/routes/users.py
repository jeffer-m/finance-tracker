from .base import APIRouter, HTTPException, Request, Depends, Session, select, uuid7, User, UserCreate, get_session, json
from .utils import check_user_exists, check_uuid

usersRouter = APIRouter(
    prefix="/users",
    tags=["users"],
)

@usersRouter.get("/{user_id}")
async def get_users(user_id, request: Request, session: Session = Depends(get_session)) -> User:
    
    if not check_uuid(user_id):
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    
    redis = request.app.state.redis
    redis_key = f"user:{user_id}"
    
    #Try fetching From Cache
    cached_user = await redis.get(redis_key)
    
    if cached_user:
        return User.model_validate_json(cached_user)
    
    user = session.exec(select(User).where(User.id == user_id)).first()
   
    if not user:
       raise HTTPException(status_code=404, detail="User not found")
   
    await redis.set(redis_key, user.model_dump_json(), ex=5)
   
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
    