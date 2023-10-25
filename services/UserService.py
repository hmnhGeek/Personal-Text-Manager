from repositories.UserRepository import UserRepository
from DTOs.User import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends

class UserService:
    def __init__(self):
        self.userRepository = UserRepository()

    def register(self, user: User):
        return self.userRepository.register(user)

    def get_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
        print("Getting")
        return self.userRepository.get_access_token(form_data)