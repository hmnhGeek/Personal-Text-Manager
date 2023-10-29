from pydantic import BaseModel
from typing import List

class PromptManagerRequestDTO(BaseModel):
    platformUrl: str
    title: str
    prompts: List[str]