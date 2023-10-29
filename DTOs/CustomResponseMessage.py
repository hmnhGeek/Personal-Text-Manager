from pydantic import BaseModel

class CustomResponseMessage(BaseModel):
    message: str
    status_code: int