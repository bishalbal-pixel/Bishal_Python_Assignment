# Question 3 - Library Management System

books = [
    {"title": "Muna Madan", "author": "Laxmi Prasad Devkota", "available": True},
    {"title": "Seto Dharti", "author": "Amar Neupane", "available": True},
    {"title": "Palpasa Cafe", "author": "Narayan Wagle", "available": False},
    {"title": "1984", "author": "George Orwell", "available": True},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "available": True},
]


def search_book(title):
    """Return the book dictionary, or raise LookupError if not found."""
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    raise LookupError(title)


def borrow_book(title):
    """Borrow a book if it is available."""
    book = search_book(title)
    if not book["available"]:
        print(f"Sorry, '{book['title']}' is already borrowed.")
    else:
        book["available"] = False
        print(f"You have borrowed '{book['title']}'.")


def return_book(title):
    """Return a borrowed book to the library."""
    book = search_book(title)
    if book["available"]:
        print(f"'{book['title']}' was not borrowed, so it cannot be returned.")
    else:
        book["available"] = True
        print(f"Thank you for returning '{book['title']}'.")


def display_available_books():
    """Print all books that are currently available."""
    print("\nAvailable Books:")
    for book in books:
        if book["available"]:
            print(f"- {book['title']} by {book['author']}")


while True:
    print("\n1. Display available books\n2. Search book\n3. Borrow book\n4. Return book\n5. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "5":
        print("Goodbye!")
        break
    if choice == "1":
        display_available_books()
        continue
    if choice not in ("2", "3", "4"):
        print("Invalid choice. Please enter 1 to 5.")
        continue

    title = input("Enter book title: ").strip()
    try:
        if choice == "2":
            book = search_book(title)
            status = "Available" if book["available"] else "Borrowed"
            print(f"Found: {book['title']} by {book['author']} ({status})")
        elif choice == "3":
            borrow_book(title)
        else:
            return_book(title)
    except LookupError:
        print(f"Error: The book '{title}' does not exist in the library.")
