class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.availability = True  # The Book is available initially

    def Checkout(self):
        self.availability = False

    def ReturnBook(self):
        self.availability = True

    def UpdateAvailability(self, new_status):
        self.availability = new_status

    def GetDetails(self):
        print(f"Title: {self.title}")
        print(f"Availability: {'Available' if self.availability else 'Checked out'}")


class Book(LibraryItem):
    def __init__(self, title, author, genre, isbn):
        super().__init__(title)
        self.author = author
        self.genre = genre
        self.isbn = isbn

    def Checkout(self):
        if self.availability:
            self.availability = False
            print(f"Book checked out: {self.title}")
        else:
            print("Book is checked out currently")

    def ReturnBook(self):
        if not self.availability:
            self.availability = True
            print(f"Book returned: {self.title}")
        else:
            print("Book is available in the library")

    def UpdateAvailability(self, new_status):
        if not self.availability:
            print("Book is currently checked out")
        else:
            self.availability = new_status
            print(f"Book availability updated: {'Available' if new_status else 'Checked out'}")

    def GetDetails(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"ISBN: {self.isbn}")
        print(f"Availability: {'Available' if self.availability else 'Checked out'}")

    def AddToLibrary(self):
        print(f"Book added to library: {self.title}")


# Creating two objects of the Book class
book1 = Book("The power of the subconcious mind", "R Madhavan", "Self Help", "9780743273565")
book2 = Book("The song of Ice and fire", "George R.R Martin", "Epic Fantasy", "9780451524935")

# Call functions on book1
book1.GetDetails()
book1.Checkout()
book1.UpdateAvailability(False)  # Trying to update availability when checked out
book1.ReturnBook()
book1.GetDetails()
book1.AddToLibrary()

print("\n")

# Call functions on book2
book2.GetDetails()
book2.Checkout()
book2.GetDetails()
book2.ReturnBook()
book2.UpdateAvailability(True)
book2.AddToLibrary()





