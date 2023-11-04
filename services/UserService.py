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
        return self.userRepository.get_access_token(form_data)

    def authenticate(self, token: str):
        return self.userRepository.authenticate(token)

    def register_token_in_session(self, token: str):
        self.userRepository.register_token_in_session(token)

    def logout(self, token: str):
        self.userRepository.logout(token)

    def is_session_active(self, username: str):
        return self.userRepository.is_session_active(username)