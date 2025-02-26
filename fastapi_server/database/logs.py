from .db_connect import DB
from bson import ObjectId
from base_models import DataInputRequest



class LogsDB:
    def __init__(self):
        self.__logs = DB().key_logs_db["logs"]

    def insert_logs(self, id: ObjectId, data: DataInputRequest):

        self.__logs.update_one(
            {'_id': id},
            {'$setOnInsert': {'_id': id}},
            upsert=True
        )

        print(data.data.items())
        
        for window, logs in data.data.items():
            safe_window = window.replace('.', '[dot]')
            self.__logs.find_one_and_update(
            {'_id': id},
            {'$set': {f'logs.{safe_window}.{data.time}': logs}}
            )

    def get_logs_for_id(self, id: ObjectId):
        return self.__logs.find_one({'_id': id })['logs']
