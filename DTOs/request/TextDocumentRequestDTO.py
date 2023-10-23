import datetime
from pydantic import BaseModel

class TextDocumentRequestDTO(BaseModel):
    heading: str
    text: str