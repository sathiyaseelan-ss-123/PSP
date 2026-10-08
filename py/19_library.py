class Library:

    def __init__(self):
        self.books = {
            "Python Programming": True,
            "Computer Networks": True,
            "Database Management": True,
            "Operating Systems": True
        }

    def display_books(self):

        print("\nAvailable Books:")

        for book, available in self.books.items():

            if available:
                print("-", book)

    def issue_book(self, book):

        if book in self.books:

            if self.books[book]:
                self.books[book] = False
                print("Book issued:", book)

            else:
                print("Book is already issued.")

        else:
            print("Book not found.")

    def return_book(self, book):

        if book in self.books:

            if not self.books[book]:
                self.books[book] = True
                print("Book returned:", book)

            else:
                print("Book was not issued.")

        else:
            print("Book not found.")