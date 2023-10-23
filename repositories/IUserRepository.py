from abc import abstractmethod
from DTOs.User import User

class IUserRepository:
    @abstractmethod
    def register(user : User) -> User: pass

    # @abstractmethod
    # def create_access_token(data : dict, expires_delta): pass

    # @abstractmethod
    # def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()): 