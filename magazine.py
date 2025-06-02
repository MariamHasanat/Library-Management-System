from libraryItem import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title: str, author: str, publication_year: int, issue_number: int):
        super().__init__(title, author, publication_year)
        self.__issue_number = issue_number
        self.__available = True  # Default availability

    def get_issue_number(self) -> int:
        return self.__issue_number

    def display_info(self) -> str:
        return f"Title: {self.get_title()}, Author: {self.get_author()}, Year: {self.get_publication_year()}, Issue Number: {self.get_issue_number()}"

    def is_available(self) -> bool:
        return self.__available

    def set_availability(self, available: bool):
        self.__available = available