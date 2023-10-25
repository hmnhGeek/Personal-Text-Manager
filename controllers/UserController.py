from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from services.UserService import UserService
from DTOs.User import User
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

user_controller_router = InferringRouter()

@cbv(user_controller_router)
class UserController:
    def __init__(self): 
        self.userService = UserService()

    @user_controller_router.post("/register")
    def register(self, user: User):
        usr = self.userService.register(user)

        if usr is not False:
            return {"message": f"User {user.username} registered successfully!"}
        else:
            raise HTTPException(status_code=422, detail="User already exists")
    
    @user_controller_router.post("/token")
    def get_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
        access_token = self.userService.get_access_token(form_data)

        if access_token is not None:
            return {"access_token": access_token, "token_type": "bearer"}
        else: raise HTTPException(status_code=400, detail="Incorrect username or password")