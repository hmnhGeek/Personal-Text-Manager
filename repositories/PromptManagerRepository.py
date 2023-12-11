from repositories.IPromptManagerRepository import IPromptManagerRepository
import os, datetime
from dotenv import load_dotenv
from DTOs.request.PromptManagerRequestDTO import PromptManagerRequestDTO, AddPromptDTO
from DTOs.response.PromptManagerResponseDTO import PromptManagerResponseDTO
from entity_manager.entity_manager import entity_manager
from DTOs.CustomResponseMessage import CustomResponseMessage
import re
from entities.PromptManager import PromptManager

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=dotenv_path)

class PromptManagerRepository(IPromptManagerRepository):
    def __init__(self):
        self.em = entity_manager.get_collection(os.environ.get("PROMPT_MANAGER_COLLECTION"))

    def add_new_prompt_object(self, promptManagerRequestDTO: PromptManagerRequestDTO, added_by: str):
        document = self.em.find_one(
            {
                "platform": re.compile(promptManagerRequestDTO.platformUrl, re.IGNORECASE),
                "title": re.compile(promptManagerRequestDTO.title, re.IGNORECASE)
            }
        )

        if document is None:
            self.em.insert_one({
                "platform": promptManagerRequestDTO.platformUrl,
                "title": promptManagerRequestDTO.title,
                "prompts": promptManagerRequestDTO.prompts,
                "username": added_by,
                "update_timestamp": datetime.datetime.now()
            })
            return promptManagerRequestDTO
        else:
            return CustomResponseMessage(status_code=409, message = "The prompt object already exists.")

    def add_prompt_to_object(self, addPromptDTO: AddPromptDTO, added_by: str) -> CustomResponseMessage:
        document = self.em.find_one(
            {
                "platform": re.compile(addPromptDTO.platformUrl, re.IGNORECASE),
                "title": re.compile(addPromptDTO.title, re.IGNORECASE),
                "username": re.compile(added_by, re.IGNORECASE),
            }
        )

        if document is not None:
            current_prompts = document["prompts"]
            current_prompts.append(addPromptDTO.prompt)

            self.em.update_one({"_id": document["_id"]}, {
                "$set": {
                    "platform": document["platform"],
                    "title": document["title"],
                    "prompts": current_prompts,
                    "username": document["username"],
                    "update_timestamp": datetime.datetime.now()
                }
            })
            return CustomResponseMessage(
                status_code = 200,
                message = "Successfully added prompt"
            )
        else:
            return CustomResponseMessage(
                status_code = 404,
                message = "The document does not exist."
            )
    
    def get_prompts_from_platform(self, platform_url: str, username: str):
        documents = self.em.find({"platform": re.compile(platform_url, re.IGNORECASE), "username": re.compile(username, re.IGNORECASE)})

        if documents is not None: 
           return [PromptManagerResponseDTO(**document) for document in documents]
        return CustomResponseMessage(
            status_code = 404,
            message = "Object not found for given platform."
        )
    
    def get_all_platforms(self, username: str):
        fields = [field for field in PromptManager.__annotations__.keys() if field != "_id"]
        
        if fields:
            unique_platforms = self.em.find({"username": re.compile(username, re.IGNORECASE)}).distinct(fields[0])
            return unique_platforms
        else:
            return CustomResponseMessage(
                status_code = 404,
                message = "No fields were found to fetch distinct details."
            )