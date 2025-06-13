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

    def check_availability(self) -> str:
        return self.get_status()

    # def set_availability(self, available: bool):
    #     self.__available = available
        
    def to_dict(self) -> dict:
        return {
            "title": self.get_title(),
            "author": self.get_author(),
            "publication_year": self.get_publication_year(),
            "issue_number": self.get_issue_number(),
            "availability": self.check_availability()
        }