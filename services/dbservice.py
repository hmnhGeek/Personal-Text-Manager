from repositories.TextRepository import TextRepository
from DTOs.request.TextDocumentRequestDTO import TextDocumentRequestDTO
from typing import List

class DBService:
    def __init__(self):
        self.text_repository = TextRepository()

    def insert_text(self, textDocumentRequestDTO : TextDocumentRequestDTO):
        self.text_repository.insert_text(textDocumentRequestDTO)

    def get_text(self, heading : str) -> List[TextDocumentRequestDTO]:
        return self.text_repository.get_text(heading)
        