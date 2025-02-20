# Encora_Assesment

Question:
Create a library management system using Python.
 The system should manage books, library members, allow for book reservations, and book loans.
Support common functionality such as
- Adding books to the library
- Registering Members
 - Loaning a Book
- Returning a Book
 If time allows, please add the following additional functionality:
- Searching
- Listing Borrowed Books
- Reserving a book
Additional Guidelines:
 * Use an object oriented approach to model and implement all of the objects and their attributes that you feel are necessary to create a library

**
Solution Approach:**

Overview

This project is a Library Management System implemented in Python using an Object-Oriented Programming (OOP) approach. The system manages books, library members, book reservations, and book loans. It supports core library functionalities such as:

1. Adding books to the library

2. Registering library members

3. Loaning books to members

4. Returning books

Additionally, the system provides extra functionalities, including:

1. Searching for books

2. Listing borrowed books

3. Reserving books

Approach

This implementation follows an OOP approach to model and manage the library system effectively. The system consists of three main classes:

1. Book Class

Represents a book in the library with attributes:

title: The title of the book

author: The author of the book

isbn: Unique identifier for the book

is_available: Boolean indicating if the book is available for loan

reserved_by: Stores the member ID if the book is reserved

2. Member Class

Represents a library member with attributes:

name: Name of the member

member_id: Unique ID assigned to each member

borrowed_books: List of books currently borrowed by the member

3. Library Class

Manages the collection of books and members, and provides methods to perform library operations, including:

Adding Books

library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")

Registering Members

library.register_member("Alice", "M001")

Loaning Books

library.loan_book("M001", "1234567890")

Returning Books

library.return_book("M001", "1234567890")

Reserving Books

library.reserve_book("M002", "0987654321")

Searching Books

library.search_books("1984")

Listing Borrowed Books

library.list_borrowed_books("M001")

**How to Use**

Clone the repository:

git clone https://github.com/yourusername/library-management-system.git


Run the Python script:

python Encora.py
