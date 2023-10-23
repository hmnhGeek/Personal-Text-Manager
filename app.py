from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.dbservice import DBService
from DTOs.request.TextDocumentRequestDTO import TextDocumentRequestDTO
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

@app.get("/")
async def root():
    return {"message": "200 OK"}

@app.post("/insert}")
def insert_text(textDocumentRequestDTO : TextDocumentRequestDTO):
    db_service.insert_text(textDocumentRequestDTO)
    return 200


if __name__ == '__main__':
    uvicorn.run("app:app",host='0.0.0.0', port=8000, reload=True)