from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.middleware.cors import CORSMiddleware
from services.dbservice import DBService
from DTOs.request.TextDocumentRequestDTO import TextDocumentRequestDTO
from typing import List
from services.UserService import UserService
from DTOs.User import User
import uvicorn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
import jwt
from controllers.UserController import user_controller_router

app = FastAPI()

tags_metadata = [
    {"name": "Users", "description": "Operations related to user management"},
    {"name": "Text", "description": "Operations related to text management"},
]

# Include the routers from controller modules
app.include_router(user_controller_router, prefix="/users", tags=["Users"])
# app.include_router(items.router, prefix="/texts", tags=["Text"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# db_service = DBService()
# user_svc = UserService()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/")
# async def root():
#     return {"message": "200 OK"}

# @app.post("/insert", tags=["Text"])
# def insert_text(textDocumentRequestDTO : TextDocumentRequestDTO, token: str = Depends(oauth2_scheme)):
#     user_svc.authenticate(token)
#     db_service.insert_text(textDocumentRequestDTO)
#     return 200

# @app.get("/{heading}", tags=["Text"])
# def get_text(heading : str, token: str = Depends(oauth2_scheme)) -> List[TextDocumentRequestDTO]:
#     user_svc.authenticate(token)
#     result = db_service.get_text(heading)
#     return result

if __name__ == '__main__':
    uvicorn.run("app:app",host='0.0.0.0', port=8001, reload=True)