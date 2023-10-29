from repositories.PromptManagerRepository import PromptManagerRepository
from DTOs.request.PromptManagerRequestDTO import PromptManagerRequestDTO, AddPromptDTO

class PromptManagerService:
    def __init__(self):
        self.promptManagerRepository = PromptManagerRepository()

    def add_new_prompt_object(self, promptManagerRequestDTO: PromptManagerRequestDTO):
        return self.promptManagerRepository.add_new_prompt_object(promptManagerRequestDTO)

    def add_prompt_to_object(self, addPromptDTO: AddPromptDTO):
        return self.promptManagerRepository.add_prompt_to_object(addPromptDTO)