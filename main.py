import json
from models.dvd import DVD
from models.user import User
import os

if __name__ == "__main__":
    path = "users.json"

    if os.path.exists(path) and os.stat(path).st_size > 0:
        with open(path, "r") as file:
            data = json.load(file)
    else:
        data = []

    dvd = DVD("Inception", "Christopher Nolan", 2010, "available", 148)
    dvd2 = DVD("Inception", "Christopher Nolan", 2010, "available", 148)
    dvd.set_status("borrowed")
    dvd2.set_status("borrowed")
    user = User(1, "John Doe", "john.doe@example.com", [dvd, dvd2])
    up_user = user.to_dict()

    data.append(up_user)

    with open(path, "w") as file:
        json.dump(data, file, indent=4)

    print(dvd.get_status())
    print(dvd.display_info())
    print(dvd.check_availability())
    print(f"DVD Title: {dvd.get_title()}")
    print(f"DVD Duration: {dvd.get_duration()} minutes")
