from pydantic import BaseModel
from typing import List

class PromptManagerRequestDTO(BaseModel):
    platformUrl: str
    title: str
    prompts: List[str]

class AddPromptDTO(BaseModel):
    platformUrl: str
    title: str
    prompt: str