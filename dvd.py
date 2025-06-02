from libraryItem import LibraryItem
from reservable import Reservable

class DVD(LibraryItem, Reservable):
    def __init__(self, title: str, director: str, publication_year: int, duration: int):
        super().__init__(title, director, publication_year)
        self.__duration = duration  # Duration in minutes
        self.__available = True  # Default availability

    def get_duration(self) -> int:
        return self.__duration

    def display_info(self) -> str:
        return f"Title: {self.get_title()}, Director: {self.get_author()}, Year: {self.get_publication_year()}, Duration: {self.get_duration()} minutes"

    def is_available(self) -> bool:
        return self.__available

    def set_availability(self, available: bool):
        self.__available = available
        
    def reserve(self, user) -> bool:
        if self.__available:
            self.__available = False
            print(f"DVD '{self.get_title()}' has been reserved by {user}.")
            return True
        else:
            print(f"DVD '{self.get_title()}' is not available for reservation.")
            return False

    def cancel_reservation(self) -> bool:
        if not self.__available:
            self.__available = True
            print(f"Reservation for DVD '{self.get_title()}' has been canceled.")
            return True
        else:
            print(f"DVD '{self.get_title()}' is not reserved.")
            return False