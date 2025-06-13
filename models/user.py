from models.libraryItem import LibraryItem

class User:
    def __init__(self, user_id: int, name: str, email: str, borrowed_items: list[LibraryItem] = []):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__borrowed_items = borrowed_items

    def get_user_id(self) -> int:
        return self.__user_id

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_borrowed_items(self) -> list:
        return self.__borrowed_items

    def add_borrowed_item(self, item: LibraryItem):
        if item not in self.__borrowed_items:
            self.__borrowed_items.append(item)

    def remove_borrowed_item(self, item: LibraryItem):
        self.__borrowed_items.remove(item)

    def to_dict(self) -> dict:
        return {
            "user_id": self.__user_id,
            "name": self.__name,
            "email": self.__email,
            "borrowed_items": [item.to_dict() for item in self.__borrowed_items]
        }