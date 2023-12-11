from repositories.PromptManagerRepository import PromptManagerRepository
from DTOs.request.PromptManagerRequestDTO import PromptManagerRequestDTO, AddPromptDTO

class PromptManagerService:
    def __init__(self):
        self.promptManagerRepository = PromptManagerRepository()

    def add_new_prompt_object(self, promptManagerRequestDTO: PromptManagerRequestDTO, added_by: str):
        return self.promptManagerRepository.add_new_prompt_object(promptManagerRequestDTO, added_by)

    def add_prompt_to_object(self, addPromptDTO: AddPromptDTO, added_by: str):
        return self.promptManagerRepository.add_prompt_to_object(addPromptDTO, added_by)

    def get_prompts_from_platform(self, platform_url: str, username: str):
        return self.promptManagerRepository.get_prompts_from_platform(platform_url, username)
    
    def get_all_platforms(self, username: str):
        return self.promptManagerRepository.get_all_platforms(username)