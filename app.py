from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.dbservice import DBService
from DTOs.request.TextDocumentRequestDTO import TextDocumentRequestDTO
from typing import List
from services.UserService import UserService
from DTOs.User import User
import uvicorn

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

@app.get("/")
async def root():
    return {"message": "200 OK"}

@app.post("/insert")
def insert_text(textDocumentRequestDTO : TextDocumentRequestDTO):
    db_service.insert_text(textDocumentRequestDTO)
    return 200

@app.get("/{heading}")
def get_text(heading : str) -> List[TextDocumentRequestDTO]:
    result = db_service.get_text(heading)
    return result

@app.post("/user/register")
def register(user: User):
    usr = user_svc.register(user)

    if usr is not False:
        return {"message": f"User {user.username} registered successfully!"}
    else:
        raise HTTPException(status_code=422, detail="User already exists")


if __name__ == '__main__':
    uvicorn.run("app:app",host='0.0.0.0', port=8000, reload=True)