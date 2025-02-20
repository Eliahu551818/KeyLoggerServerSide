from fastapi import APIRouter
from base_models import DataInputRequest
from database import LogsDB, UserDB
from bson import ObjectId
from fastapi.responses import JSONResponse


router = APIRouter()

users = UserDB()
logs = LogsDB()


@router.post("/data/insert_data", tags=["Data"])
async def add_data(data: DataInputRequest):
    user = users.get_user_by_mac_address(data.mac_address)
    logs.insert_logs(user.get('_id'), data=data)
    return JSONResponse(content=True)

@router.get('/data/get_logs_for_user', tags=["data"])
async def get_logs_for_user(id: str):
    user_logs = logs.get_logs_for_id(ObjectId(id))
    return JSONResponse(content={'logs': user_logs})