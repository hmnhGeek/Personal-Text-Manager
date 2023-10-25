from abc import abstractmethod
from DTOs.User import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends

class IUserRepository:
    @abstractmethod
    def register(self, user : User) -> User: pass

    @abstractmethod
    def create_access_token(self, data: dict, expires_delta): pass

    @abstractmethod
    def get_user(self, username: str): pass

    @abstractmethod
    def get_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()): pass

    @abstractmethod
    def authenticate(self, token: str): pass
