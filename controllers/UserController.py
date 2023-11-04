from fastapi import HTTPException, Depends, Header
from fastapi.security import OAuth2PasswordRequestForm
from services.UserService import UserService
from DTOs.User import User
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from DTOs.CustomResponseMessage import CustomResponseMessage

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
        if not self.userService.is_session_active(form_data.username):
            access_token = self.userService.get_access_token(form_data)

            if access_token is not None:
                self.userService.register_token_in_session(access_token)
                return {"access_token": access_token, "token_type": "bearer"}
            else: raise HTTPException(status_code=400, detail="Incorrect username or password")
        else:
            return CustomResponseMessage(status_code = 200, message = "Session already active")

    @user_controller_router.post("/logout")
    def logout(self, token: str = Header(None)):
        if token is None: raise HTTPException(status_code=401, detail="Invalid token")
        self.userService.logout(token)
        return CustomResponseMessage(status_code = 200, message = "Logged out successfully")