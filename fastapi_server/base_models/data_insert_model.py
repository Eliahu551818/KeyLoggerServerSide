# Defines the input class with the required fields to be able to inser data
from pydantic import BaseModel

class DataInputRequest(BaseModel):
    mac_address: str
    time: str
    data: dict
    nickname: str