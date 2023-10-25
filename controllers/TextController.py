from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from services.dbservice import DBService
from DTOs.request.TextDocumentRequestDTO import TextDocumentRequestDTO
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from services.UserService import UserService
from typing import List

text_controller_router = InferringRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

@cbv(text_controller_router)
class TextController:
    def __init__(self):
        self.dbService = DBService()
        self.userService = UserService()

    @text_controller_router.post("/insert")
    def insert_text(self, textDocumentRequestDTO : TextDocumentRequestDTO, token: str = Depends(oauth2_scheme)):
        self.userService.authenticate(token)
        self.dbService.insert_text(textDocumentRequestDTO)
        return 200

    @text_controller_router.get("/{heading}")
    def get_text(self, heading : str, token: str = Depends(oauth2_scheme)) -> List[TextDocumentRequestDTO]:
        self.userService.authenticate(token)
        result = self.dbService.get_text(heading)
        return result