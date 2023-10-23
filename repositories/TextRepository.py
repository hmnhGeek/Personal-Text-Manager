from repositories.ITextRepository import ITextRepository
from entity_manager.entity_manager import entity_manager
import os, datetime
from dotenv import load_dotenv
from DTOs.request.TextDocumentRequestDTO import TextDocumentRequestDTO

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=dotenv_path)

class TextRepository(ITextRepository):
    def __init__(self):
        self.em = entity_manager
        self.dump_collection = os.environ.get("COLLECTION")

    def insert_text(self, textDocumentRequestDTO : TextDocumentRequestDTO):
        self.em.get_collection(self.dump_collection).insert_one(
            {
                "heading": textDocumentRequestDTO.heading,
                "text": textDocumentRequestDTO.text,
                "timestamp": datetime.datetime.now()
            }
        )