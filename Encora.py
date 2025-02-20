class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.reserved_by = None

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book added: {book}")

    def register_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Member registered: {member}")

    def loan_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if book and member:
            if book.is_available:
                book.is_available = False
                member.borrowed_books.append(book)
                print(f"Book loaned: {book} to {member}")
            elif book.reserved_by == member_id:
                book.is_available = False
                book.reserved_by = None
                member.borrowed_books.append(book)
                print(f"Reserved book loaned: {book} to {member}")
            else:
                print("Book is currently not available.")
        else:
            print("Invalid member ID or book ISBN.")

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)

        if member:
            for book in member.borrowed_books:
                if book.isbn == isbn:
                    book.is_available = True
                    member.borrowed_books.remove(book)
                    print(f"Book returned: {book} by {member}")
                    return
            print("Book not found in member's borrowed list.")
        else:
            print("Member not found.")

    def reserve_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if book and member:
            if book.is_available:
                print("Book is available. No need to reserve.")
            elif book.reserved_by is None:
                book.reserved_by = member_id
                print(f"Book reserved: {book} by {member}")
            else:
                print("Book is already reserved.")
        else:
            print("Invalid member ID or book ISBN.")

    def search_books(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if results:
            print("Search results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def list_borrowed_books(self, member_id):
        member = self.find_member(member_id)
        if member:
            if member.borrowed_books:
                print(f"Books borrowed by {member}:")
                for book in member.borrowed_books:
                    print(book)
            else:
                print("No books borrowed.")
        else:
            print("Member not found.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


library = Library()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
library.add_book("1984", "George Orwell", "0987654321")

library.register_member("Alice", "M001")
library.register_member("Bob", "M002")

library.loan_book("M001", "1234567890")
library.list_borrowed_books("M001")

library.return_book("M001", "1234567890")
library.reserve_book("M002", "0987654321")


library = Library()
library.add_book("The Guide", "R. K. Narayan", "1234567890")
library.add_book("Train to Pakistan", "Khushwant Singh", "0987654321")
library.add_book("Wings of Fire", "A. P. J. Abdul Kalam", "1122334455")

library.register_member("Rajesh Kumar", "M001")
library.register_member("Priya Sharma", "M002")

library.loan_book("M001", "1234567890")
library.list_borrowed_books("M001")

library.return_book("M001", "1234567890")
library.reserve_book("M002", "0987654321")

