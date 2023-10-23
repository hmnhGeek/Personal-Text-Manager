from repositories.IUserRepository import IUserRepository
from entity_manager.entity_manager import entity_manager
from DTOs.User import User
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=dotenv_path)

class UserRepository(IUserRepository):
    def __init__(self):
        self.em = entity_manager.get_collection(os.environ.get("USER_COLLECTION"))
    
    def register(self, user : User):
        usr = self.em.find_one({"username": user.username})

        if usr is None:
            self.em.insert_one(
                {
                    "username": user.username,
                    "password": user.password
                }
            )
            return user
        else:
            return False