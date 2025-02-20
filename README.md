# Library Management System

## Overview
This project is a **Library Management System** implemented in Python using an **Object-Oriented Programming (OOP)** approach. The system manages books, library members, book reservations, and book loans. It supports core library functionalities such as:

- Adding books to the library
- Registering library members
- Loaning books to members
- Returning books

Additionally, the system provides extra functionalities, including:

- Searching for books
- Listing borrowed books
- Reserving books

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributions](#contributions)

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/Sachinjha469/Encora_Assesment.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Encora_Assesment
   ```
3. Run the Python script:
   ```sh
   python library.py
   ```

## Usage
- **Adding Books**
  ```python
  library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
  ```
- **Registering Members**
  ```python
  library.register_member("Alice", "M001")
  ```
- **Loaning Books**
  ```python
  library.loan_book("M001", "1234567890")
  ```
- **Returning Books**
  ```python
  library.return_book("M001", "1234567890")
  ```
- **Searching Books**
  ```python
  library.search_books("1984")
  ```

## Features
- Book management (add, search, loan, return, and reserve books)
- Member management (register, list borrowed books)
- Book reservation system


## Contributions
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

