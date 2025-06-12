from abc import ABC, abstractmethod
from models.itemStatus import ItemStatus

class LibraryItem(ABC):
    def __init__(self, title: str, author: str, publication_year: int, status: ItemStatus):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__status = status
        
    def get_status(self) -> ItemStatus:
        return self.__status

    def set_status(self, status: ItemStatus):
        self.__status = status
        
    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_publication_year(self) -> int:
        return self.__publication_year

    @abstractmethod
    def display_info(self) -> str:
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        pass