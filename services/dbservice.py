from repositories.TextRepository import TextRepository
from DTOs.request.TextDocumentRequestDTO import TextDocumentRequestDTO

class DBService:
    def __init__(self):
        self.text_repository = TextRepository()

    def insert_text(self, textDocumentRequestDTO : TextDocumentRequestDTO):
        self.text_repository.insert_text(textDocumentRequestDTO)
        