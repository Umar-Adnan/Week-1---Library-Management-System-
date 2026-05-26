
# ==============================
# LIBRARY MANAGEMENT SYSTEM (CLI)
# ==============================

import json
from datetime import datetime, timedelta
import os

# ------------------------------
# FILES
# ------------------------------

BOOKS_FILE = "books.json"
TRANSACTIONS_FILE = "transactions.json"

# ------------------------------
# CREATE FILES IF NOT EXIST
# ------------------------------

if not os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "w") as f:
        json.dump([], f)

if not os.path.exists(TRANSACTIONS_FILE):
    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump([], f)

# ------------------------------
# BOOK CLASS
# ------------------------------

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }

# ------------------------------
# PERSON CLASS
# ------------------------------

class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

# ------------------------------
# ADMIN CLASS
# ------------------------------

class Admin(Person):

    def add_book(self):

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)

        books = load_books()
        books.append(book.to_dict())

        save_books(books)

        print("\nBook added successfully!\n")

    def remove_book(self):

        book_id = input("Enter Book ID to remove: ")

        books = load_books()

        updated_books = [book for book in books if book["book_id"] != book_id]

        save_books(updated_books)

        print("\nBook removed successfully!\n")

# ------------------------------
# MEMBER CLASS
# ------------------------------

class Member(Person):

    def borrow_book(self):

        book_id = input("Enter Book ID to borrow: ")

        books = load_books()

        for book in books:

            if book["book_id"] == book_id:

                if book["available"]:

                    book["available"] = False

                    save_books(books)

                    transaction = {
                        "member_id": self.person_id,
                        "book_id": book_id,
                        "borrow_date": str(datetime.now()),
                        "return_date": None
                    }

                    transactions = load_transactions()
                    transactions.append(transaction)

                    save_transactions(transactions)

                    print("\nBook borrowed successfully!\n")
                    return

                else:
                    print("\nBook is already borrowed.\n")
                    return

        print("\nBook not found.\n")

    def return_book(self):

        book_id = input("Enter Book ID to return: ")

        books = load_books()

        for book in books:

            if book["book_id"] == book_id:

                book["available"] = True

        save_books(books)

        transactions = load_transactions()

        for transaction in transactions:

            if transaction["book_id"] == book_id and transaction["return_date"] is None:

                borrow_date = datetime.fromisoformat(transaction["borrow_date"])

                return_date = datetime.now()

                transaction["return_date"] = str(return_date)

                # LATE FEE LOGIC

                allowed_days = 7

                days_borrowed = (return_date - borrow_date).days

                if days_borrowed > allowed_days:

                    late_days = days_borrowed - allowed_days
                    fine = late_days * 50

                    print(f"\nLate Return!")
                    print(f"Fine = Rs.{fine}")

                else:
                    print("\nBook returned successfully with no fine.")

        save_transactions(transactions)

# ------------------------------
# FILE HANDLING FUNCTIONS
# ------------------------------

def load_books():

    with open(BOOKS_FILE, "r") as f:
        return json.load(f)

def save_books(books):

    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

def load_transactions():

    with open(TRANSACTIONS_FILE, "r") as f:
        return json.load(f)

def save_transactions(transactions):

    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump(transactions, f, indent=4)

# ------------------------------
# DISPLAY BOOKS
# ------------------------------

def view_books():

    books = load_books()

    if not books:
        print("\nNo books available.\n")
        return

    print("\n===== BOOK LIST =====\n")

    for book in books:

        status = "Available" if book["available"] else "Borrowed"

        print(f"""
Book ID : {book['book_id']}
Title   : {book['title']}
Author  : {book['author']}
Status  : {status}
""")

# ------------------------------
# SEARCH BOOK
# ------------------------------

def search_book():

    keyword = input("Enter title or author: ").lower()

    books = load_books()

    found = False

    for book in books:

        if keyword in book["title"].lower() or keyword in book["author"].lower():

            found = True

            print(f"""
Book ID : {book['book_id']}
Title   : {book['title']}
Author  : {book['author']}
""")

    if not found:
        print("\nNo matching books found.\n")

# ------------------------------
# MAIN MENU
# ------------------------------

admin = Admin("A1", "Admin")
member = Member("M1", "Umar")

while True:

    print("""
===== LIBRARY MANAGEMENT SYSTEM =====

1. View Books
2. Add Book
3. Remove Book
4. Borrow Book
5. Return Book
6. Search Book
7. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_books()

    elif choice == "2":
        admin.add_book()

    elif choice == "3":
        admin.remove_book()

    elif choice == "4":
        member.borrow_book()

    elif choice == "5":
        member.return_book()

    elif choice == "6":
        search_book()

    elif choice == "7":
        print("\nExiting Library System...")
        break

    else:
        print("\nInvalid choice.\n")

