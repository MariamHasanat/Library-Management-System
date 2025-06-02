from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title: str, author: str, publication_year: int):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        
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