# Library Management System

A command-line (CLI) library management application built with Python. It lets an admin manage the book catalog and lets members borrow and return books, with automatic late-fee calculation on returns.

## Features

- **View books** — List all books with availability status (Available / Borrowed)
- **Add book** — Admin adds new books to the catalog
- **Remove book** — Admin removes books by Book ID
- **Borrow book** — Members borrow available books; availability is updated and a transaction is recorded
- **Return book** — Members return books; availability is restored and late fees are calculated if applicable
- **Search books** — Find books by title or author (partial, case-insensitive match)
- **Persistent storage** — Data is saved to JSON files (`books.json`, `transactions.json`)

## Requirements

- Python 3.x
- No external packages (uses only the standard library: `json`, `datetime`, `os`)

## Project Structure

```
Project Week 1/
├── Library Management System.py   # Main application
├── books.json                     # Book catalog (auto-created if missing)
├── transactions.json              # Borrow/return history (auto-created if missing)
└── README.md
```

## How to Run

1. Open a terminal in the `Project Week 1` folder.
2. (Optional) Activate the virtual environment if you use one:
   ```bash
   .venv\Scripts\activate
   ```
3. Run the application:
   ```bash
   python "Library Management System.py"
   ```

On first run, `books.json` and `transactions.json` are created automatically if they do not exist.

## Menu Options

| Option | Action        | Role   |
|--------|---------------|--------|
| 1      | View Books    | All    |
| 2      | Add Book      | Admin  |
| 3      | Remove Book   | Admin  |
| 4      | Borrow Book   | Member |
| 5      | Return Book   | Member |
| 6      | Search Book   | All    |
| 7      | Exit          | All    |

## Object-Oriented Design

The application uses inheritance and role-based classes:

| Class    | Extends  | Responsibility                                      |
|----------|----------|-----------------------------------------------------|
| `Person` | —        | Base class with `person_id` and `name`              |
| `Admin`  | `Person` | Add and remove books                                |
| `Member` | `Person` | Borrow and return books                             |
| `Book`   | —        | Represents a book (`book_id`, `title`, `author`, `available`) |

Default users in the script:

- **Admin:** ID `A1`, name `Admin`
- **Member:** ID `M1`, name `Umar`

## Data Model

### Book (`books.json`)

Each book is stored as:

```json
{
    "book_id": "101",
    "title": "Atomic Habits",
    "author": "James Clear",
    "available": true
}
```

### Transaction (`transactions.json`)

Each borrow/return is recorded as:

```json
{
    "member_id": "M1",
    "book_id": "101",
    "borrow_date": "2026-05-26 10:30:00.123456",
    "return_date": null
}
```

When a book is returned, `return_date` is set and late fees may apply.

## Late Fee Policy

- **Allowed borrow period:** 7 days
- **Fine:** Rs. 50 per day after the allowed period
- On return, if the book is overdue, the system prints the late fee; otherwise it confirms a successful return with no fine.

## Example Workflow

1. **Add a book** — Choose option `2`, enter Book ID, title, and author.
2. **View catalog** — Choose option `1` to see all books and status.
3. **Borrow** — Choose option `4`, enter a Book ID for an available book.
4. **Return** — Choose option `5`, enter the same Book ID; late fees are calculated automatically if overdue.
5. **Search** — Choose option `6`, enter part of a title or author name.

## Notes

- Book IDs must be unique; removing or borrowing uses the Book ID you enter.
- A book cannot be borrowed if it is already marked as borrowed.
- Search matches substrings in title or author (case-insensitive).

---

*Week 1 project — Afyniix Digital internship*
