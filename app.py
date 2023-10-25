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

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_service = DBService()
user_svc = UserService()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "200 OK"}

@app.post("/insert")
def insert_text(textDocumentRequestDTO : TextDocumentRequestDTO, token: str = Depends(oauth2_scheme)):
    status = user_svc.authenticate(token)

    if status == 400: raise HTTPException(status_code=400, detail="Could not validate credentials, user not found.")
    if status == 401: raise HTTPException(status_code=401, detail="Authentication failed, invalid or expired token.")
    
    db_service.insert_text(textDocumentRequestDTO)
    return 200

@app.get("/{heading}")
def get_text(heading : str, token: str = Depends(oauth2_scheme)) -> List[TextDocumentRequestDTO]:
    status = user_svc.authenticate(token)

    if status == 400: raise HTTPException(status_code=400, detail="Could not validate credentials, user not found.")
    if status == 401: raise HTTPException(status_code=401, detail="Authentication failed, invalid or expired token.")

    result = db_service.get_text(heading)
    return result

@app.post("/user/register")
def register(user: User):
    usr = user_svc.register(user)

    if usr is not False:
        return {"message": f"User {user.username} registered successfully!"}
    else:
        raise HTTPException(status_code=422, detail="User already exists")

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    access_token = user_svc.get_access_token(form_data)

    if access_token is not None:
        return {"access_token": access_token, "token_type": "bearer"}
    else: raise HTTPException(status_code=400, detail="Incorrect username or password")

if __name__ == '__main__':
    uvicorn.run("app:app",host='0.0.0.0', port=8000, reload=True)