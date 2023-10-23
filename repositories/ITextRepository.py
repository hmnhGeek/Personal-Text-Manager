from abc import abstractmethod

class ITextRepository:
    @abstractmethod
    def insert_text(self, heading, text): pass
