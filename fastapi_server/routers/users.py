from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database import LogsDB, UserDB
from .utils import serialize_id
import json

router = APIRouter()

users = UserDB()
logs = LogsDB()

@router.get('/users/list_of_users', tags=['User'])
async def get_list_of_users():
    """
    Retrieve a list of all users.

    Returns:
        dict: A dictionary containing a list of serialized users.
    """
    """
    Retrieve a list of all users.

    This endpoint returns a list of all users in the database,
    with each user's ID serialized for frontend compatibility.
    """
    all_users = users.get_all_users() # 
    serialized_users = [serialize_id(user) for user in all_users]
    return JSONResponse(content={"users": serialized_users})