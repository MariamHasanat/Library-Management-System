from models.dvd import DVD

if __name__ == "__main__":
    dvd = DVD("Inception", "Christopher Nolan", 2010, "available", 148)
    print(dvd.get_status())
    print(dvd.display_info())
    print(dvd.check_availability())
  
    
    # Example of using the DVD class
    print(f"DVD Title: {dvd.get_title()}")
    print(f"DVD Duration: {dvd.get_duration()} minutes")