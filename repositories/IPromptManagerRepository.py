from abc import abstractmethod
from DTOs.request.PromptManagerRequestDTO import PromptManagerRequestDTO, AddPromptDTO
from DTOs.CustomResponseMessage import CustomResponseMessage

class IPromptManagerRepository:
    @abstractmethod
    def add_new_prompt_object(self, promptManagerRequestDTO: PromptManagerRequestDTO): pass

    @abstractmethod
    def add_prompt_to_object(self, addPromptDTO: AddPromptDTO) -> CustomResponseMessage: pass

    @abstractmethod
    def get_prompts_from_platform(self, platform_url: str): pass

    @abstractmethod
    def get_all_platforms(self): pass