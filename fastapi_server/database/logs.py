from .db_connect import DB
from bson import ObjectId
from base_models import DataInputRequest

class LogsDB:
    def __init__(self):
        self.__logs = DB().key_logs_db["logs"]

    def insert_logs(self, id: ObjectId, data: DataInputRequest):
        for window, logs in data.data.items():
            self.__logs.find_one_and_update({'_id': id }, {'$set':{ f'logs.{window}.{data.time}' : logs } })

    def show_logs(self, id: ObjectId):
        return self.__logs.find_one({'_id': id })['logs']
