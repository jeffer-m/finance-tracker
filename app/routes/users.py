from fastapi import APIRouter

usersRouter = APIRouter(
    prefix="/users",
    tags=["users"],
)

@usersRouter.get("")
def get_users():
    return {"message": "List of users"}