from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId

class PromptManagerResponseDTO(BaseModel):
    _id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    platform: str
    title: str
    prompts: List[str]