from .db_connect import DB
import time

class UserDB:
    def __init__(self):
        self.__users = DB().key_logs_db["users"]

    def inser_new_user(self, nickname: str, mac_address: str, **kwargs):
        new_user = self.__users.insert_one(
            {
                'nickname': nickname,
                'mac_address': mac_address,
                'created_at': time.strftime("%Y-%m-%d %H:%M:%S") 
            })
        
        if new_user.inserted_id:
            return (True, new_user.inserted_id)
        
    def get_user_by_mac_address(self, mac_address: str):
        return self.__users.find_one({'mac_address': mac_address })

    def get_all_users(self):
        return self.__users.find(projection=['nickname', 'mac_address'])
    
    

        




