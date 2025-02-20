from fastapi import APIRouter
from base_models import DataInputRequest
from database import LogsDB, UserDB

router = APIRouter()

users = UserDB()
logs = LogsDB()

@router.post("/data/insert_data", tags=["data"])
async def add_data(data: DataInputRequest):

    user = users.get_user_by_mac_address(data.mac_address)
    logs.insert_logs(user.get('_id'), data=data)
    return True


# l = LogsDB()
# l.insert_logs(ObjectId('67b706636b4a774096b8707e'), {
#     DataInputRequest(mac_address='f3:a3:d4:e5:22:12', time=time.strftime("%Y-%m-%d %H:%M"), data={ 'Desktop': ['p','a','s','s','w','o','r','d']})
# })
        