from repositories.ITextRepository import ITextRepository
from entity_manager.entity_manager import entity_manager
import os, datetime
from dotenv import load_dotenv
from DTOs.request.TextDocumentRequestDTO import TextDocumentRequestDTO
from typing import List
from pymongo import DESCENDING

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=dotenv_path)

class TextRepository(ITextRepository):
    def __init__(self):
        self.em = entity_manager.get_collection(os.environ.get("COLLECTION"))

    def insert_text(self, textDocumentRequestDTO : TextDocumentRequestDTO):
        self.em.insert_one(
            {
                "heading": textDocumentRequestDTO.heading,
                "text": textDocumentRequestDTO.text,
                "timestamp": datetime.datetime.now()
            }
        )

    def get_text(self, heading : str) -> List[TextDocumentRequestDTO]:
        documents = list(self.em.find({"heading": heading}).sort(
            [("timestamp", DESCENDING)]
        ))
        result = []
        
        for document in documents:
            result.append(
                TextDocumentRequestDTO(
                    heading = document["heading"],
                    text = document["text"],
                )
            )

        return result