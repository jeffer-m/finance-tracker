from fastapi import FastAPI
from app.routes.users import usersRouter

app = FastAPI()

app.include_router(usersRouter)

@app.get("/")
def default():
    return {"message": "Hello World"}