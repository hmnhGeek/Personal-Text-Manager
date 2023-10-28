from abc import abstractmethod
from DTOs.request.PromptManagerRequestDTO import PromptManagerRequestDTO

class IPromptManagerRepository:
    @abstractmethod
    def add_new_prompt_object(self, promptManagerRequestDTO: PromptManagerRequestDTO): pass