# Base class 
class LibraryItem:
    def __init__(self, title):
        self.title = title
    
    def get_details(self):
        print(f"Title: {self.title}")

# Derived class Magazine
class Magazine(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number
    
    def get_details(self):
        print(f"Title: {self.title}")
        print(f"Issue Number: {self.issue_number}")

# Derived class DVD
class DVD(LibraryItem):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration
    
    def get_details(self):
        print(f"Title: {self.title}")
        print(f"Duration: {self.duration} minutes")

# Creating an object of Magazine
magazine = Magazine("Intrestellar", 202)
magazine.get_details()

print("\n")

# Creating an object of DVD
dvd = DVD("Inception", 148)
dvd.get_details()

