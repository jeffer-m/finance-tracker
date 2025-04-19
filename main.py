from fastapi import FastAPI
from app.routes.users import usersRouter
from app.models.users import User
from contextlib import asynccontextmanager
from app.services.db import init_db, get_session
from app.services.redis_service import init_redis



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    
    app.state.redis = await init_redis()
    
    yield
    
    #cleanup
    if hasattr(app.state, "redis"):
        await app.state.redis.close()
    
app = FastAPI(lifespan=lifespan)

app.include_router(usersRouter)

@app.get("/")
def default():
    return {"message": "Hello World"}
