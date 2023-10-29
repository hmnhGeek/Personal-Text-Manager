from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from services.PromptManagerService import PromptManagerService
from services.UserService import UserService
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from DTOs.request.PromptManagerRequestDTO import PromptManagerRequestDTO

prompt_manager_controller_router = InferringRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

@cbv(prompt_manager_controller_router)
class PromptManagerController:
    def __init__(self):
        self.promptManagerService = PromptManagerService()
        self.userService = UserService()
    
    @prompt_manager_controller_router.post("/add_new_prompt_object")
    def add_new_prompt_object(self, promptManagerRequestDTO: PromptManagerRequestDTO, token: str = Depends(oauth2_scheme)):
        self.userService.authenticate(token)
        return self.promptManagerService.add_new_prompt_object(promptManagerRequestDTO)