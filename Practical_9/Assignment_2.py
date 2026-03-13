# Lab Assignment - Library Management System
# Shivam Dipte

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added to library.")

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Member '{name}' added to library.")

    def show_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for book in self.books:
                book.display_info()


def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Show Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)

        elif choice == "2":
            name = input("Enter member name: ")
            library.add_member(name)

        elif choice == "3":
            library.show_books()

        elif choice == "4":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            member = next((m for m in library.members if m.name == member_name), None)
            book = next((b for b in library.books if b.title == book_title), None)
            if member and book:
                member.borrow_book(book)
            else:
                print("Member or Book not found.")

        elif choice == "5":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            member = next((m for m in library.members if m.name == member_name), None)
            book = next((b for b in library.books if b.title == book_title), None)
            if member and book:
                member.return_book(book)
            else:
                print("Member or Book not found.")

        elif choice == "6":
            print("Exiting Library System...")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()