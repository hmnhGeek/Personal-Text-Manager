from repositories.UserRepository import UserRepository
from DTOs.User import User

class UserService:
    def __init__(self):
        self.userRepository = UserRepository()

    def register(self, user: User):
        return self.userRepository.register(user)