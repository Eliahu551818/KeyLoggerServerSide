import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

uri = os.environ.get("MONGO_URI")

if not uri:
	raise ValueError("MONGO_URI environment variable is not set")

class DB:
    def __init__(self):
        self.__cluster = MongoClient(uri)
        self.key_logs_db = self.__cluster["KeyLogs"]
		
	




  


