from repositories.IPromptManagerRepository import IPromptManagerRepository
import os, datetime
from dotenv import load_dotenv
from DTOs.request.PromptManagerRequestDTO import PromptManagerRequestDTO
from entity_manager.entity_manager import entity_manager
from DTOs.CustomResponseMessage import CustomResponseMessage

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=dotenv_path)

class PromptManagerRepository(IPromptManagerRepository):
    def __init__(self):
        self.em = entity_manager.get_collection(os.environ.get("PROMPT_MANAGER_COLLECTION"))

    def add_new_prompt_object(self, promptManagerRequestDTO: PromptManagerRequestDTO):
        document = self.em.find_one({"platform": promptManagerRequestDTO.platformUrl})

        if document is None:
            self.em.insert_one({
                "platform": promptManagerRequestDTO.platformUrl,
                "title": promptManagerRequestDTO.title,
                "prompts": promptManagerRequestDTO.prompts,
                "update_timestamp": datetime.datetime.now()
            })
            return promptManagerRequestDTO
        else:
            return CustomResponseMessage(status_code=401, message = "The prompt object already exists.")