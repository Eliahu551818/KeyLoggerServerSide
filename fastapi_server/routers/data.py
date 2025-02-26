from fastapi import APIRouter, Query
from base_models import DataInputRequest
from database import LogsDB, UserDB
from bson import ObjectId
from fastapi.responses import JSONResponse
from typing import Optional


router = APIRouter()

users = UserDB()
logs = LogsDB()


@router.post("/data/insert_data", tags=["Data"])
async def add_data(data: DataInputRequest):
    print(data.mac_address)
    user = users.get_user_by_mac_address(data.mac_address)
    logs.insert_logs(user.get('_id'), data=data)
    return JSONResponse(content={"success": True})

@router.get('/data/get_logs_for_user', tags=["data"])
async def get_logs_for_user(
    id: str,
    from_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    to_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)"),
    window: Optional[str] = Query(None, description="Window name")
):
    # Build filter dict only with provided parameters
    filter_params = {}
    if from_date:
        filter_params["from_date"] = from_date
    if to_date:
        filter_params["to_date"] = to_date
    if window:
        filter_params["window"] = window

    # Call the logs function with or without filters
    if filter_params:
        user_logs = logs.get_logs_for_id(ObjectId(id), fil=filter_params)
    else:
        user_logs = logs.get_logs_for_id(ObjectId(id))

    return JSONResponse(content={'logs': user_logs})