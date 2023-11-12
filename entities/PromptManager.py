from pydantic import BaseModel
from typing import List
import datetime
from bson import ObjectId

class PromptManager(BaseModel):
    _id: ObjectId
    platform: str
    title: str
    prompts: List[str]
    update_timestamp: datetime.datetime