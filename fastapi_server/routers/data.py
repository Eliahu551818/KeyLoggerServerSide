from fastapi import APIRouter, Query, HTTPException
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
    user = users.get_user_by_mac_address(data.mac_address, data.nickname)
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
    if from_date != None:
        filter_params["from_date"] = from_date
    if to_date != None:
        filter_params["to_date"] = to_date
    if window != None:
        filter_params["window"] = window

    # Call the logs function with or without filters
    if filter_params:
        user_logs = logs.get_logs_for_id(ObjectId(id), fil=filter_params)
    else:
        user_logs = logs.get_logs_for_id(ObjectId(id))

    return JSONResponse(content={'logs': user_logs})

@router.get('/data/stats', tags=['data'])
async def get_stats(
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
    try:
        if filter_params:
            logs_data = logs.get_logs_for_id(ObjectId(id), fil=filter_params)
        else:
            logs_data = logs.get_logs_for_id(ObjectId(id))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching logs: {str(e)}")

    if not logs_data:
        raise HTTPException(status_code=404, detail="User not found")

    # Calculate statistics using the stats.py function
    stats = logs.calculate_statistics(logs_data)
    return stats