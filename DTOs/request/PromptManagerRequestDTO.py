from pydantic import BaseModel
from typing import List

class PromptManagerRequestDTO:
    platformUrl: str
    title: str
    prompts: List[str]