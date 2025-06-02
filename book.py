from libraryItem import LibraryItem
from reservable import Reservable

class Book(LibraryItem, Reservable):
    def __init__(self, title: str, author: str, publication_year: int, isbn: str):
        super().__init__(title, author, publication_year)
        self.__isbn = isbn
        self.__available = True  # Default availability

    def get_isbn(self) -> str:
        return self.__isbn

    def display_info(self) -> str:
        return f"Title: {self.get_title()}, Author: {self.get_author()}, Year: {self.get_publication_year()}, ISBN: {self.get_isbn()}"

    def is_available(self) -> bool:
        return self.__available

    def set_availability(self, available: bool):
        self.__available = available
        
    def reserve(self, user) -> bool:
        if self.__available:
            self.__available = False
            print(f"Book '{self.get_title()}' has been reserved by {user}.")
            return True
        else:
            print(f"Book '{self.get_title()}' is not available for reservation.")
            return False

    def cancel_reservation(self) -> bool:
        if not self.__available:
            self.__available = True
            print(f"Reservation for book '{self.get_title()}' has been canceled.")
            return True
        else:
            print(f"Book '{self.get_title()}' is not reserved.")
            return False