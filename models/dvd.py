from models.libraryItem import LibraryItem
from models.itemStatus import ItemStatus
from models.reservable import Reservable

class DVD(LibraryItem, Reservable):
    def __init__(self, title: str, author: str, publication_year: int, status: ItemStatus, duration: int):
        super().__init__(title, author, publication_year, status)
        self.__duration = duration  # Duration in minutes
       
    def display_info(self) -> str:
        return f"Title: {self.get_title()}, Author: {self.get_author()}, Year: {self.get_publication_year()}, Duration: {self.get_duration()} minutes"

    def check_availability(self) -> str:
        return self.get_status()
    
    def reserve(self, user) -> bool: #need more implementation details for user - remember this is a library system
        if self.get_status() == ItemStatus.AVAILABLE:
            self.set_status(ItemStatus.RESERVED)
            print(f"DVD '{self.get_title()}' has been reserved by {user}.")
            return True
        else:
            print(f"DVD '{self.get_title()}' is not available for reservation.")
            return False


# ----------------------------------------------------------
    def get_duration(self) -> int:
        return self.__duration
# ----------------------------------------------------------
    # def cancel_reservation(self) -> bool:
    #     if not self.get_status() == ItemStatus.AVAILABLE:
    #         self.set_status(ItemStatus.AVAILABLE)
    #         print(f"Reservation for DVD '{self.get_title()}' has been canceled.")
    #         return True
    #     else:
    #         print(f"DVD '{self.get_title()}' is not reserved.")
    #         return False