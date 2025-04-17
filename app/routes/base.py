from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select, Session
from app.models.users import User, UserCreate
from app.services.db import get_session
from uuid6 import uuid7, UUID