from .base import SQLModel, Field, UUID, uuid7


class UserBase(SQLModel):
    username: str = Field(max_length=50, nullable=False, unique=True)
    
class UserLogin(UserBase):
    password: str = Field(max_length=100, nullable=False)
    
class UserCreate(UserLogin):
    name: str = Field(max_length=50, nullable=False)
    surname: str = Field(max_length=50, nullable=False)
    email: str = Field(max_length=100, nullable=False, unique=True)

class User(UserCreate, table=True):
    id: UUID = Field(default_factory=uuid7, primary_key=True)
    
    
    
