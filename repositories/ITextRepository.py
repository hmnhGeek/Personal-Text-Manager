from abc import abstractmethod

class ITextRepository:
    @abstractmethod
    def insert_text(self, heading, text): pass

    @abstractmethod
    def get_text(self, heading): pass
