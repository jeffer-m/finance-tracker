from fastapi import FastAPI
from app.routes.users import usersRouter
from app.models.users import User
from contextlib import asynccontextmanager
from app.services.db import init_db, get_session



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(usersRouter)

@app.get("/")
def default():
    return {"message": "Hello World"}
