from database import create_connection
import datetime

def add_book(title, author, isbn, quantity):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO books (title, author, isbn, quantity, available)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, author, isbn, quantity, quantity))
        conn.commit()
        print("Book added successfully!")
    except Exception as e:
        print("Error: ISBN already exists!")
    finally:
        conn.close()

def add_member(name, email, phone):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO members (name, email, phone)
            VALUES (?, ?, ?)
        ''', (name, email, phone))
        conn.commit()
        print("Member added successfully!")
    except Exception as e:
        print("Error: Email already exists!")
    finally:
        conn.close()

def borrow_book(book_id, member_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        # Check if book is available
        cursor.execute('SELECT available FROM books WHERE book_id = ?', (book_id,))
        available = cursor.fetchone()[0]
        
        if available > 0:
            # Add borrowing record
            borrow_date = datetime.date.today()
            cursor.execute('''
                INSERT INTO borrowings (book_id, member_id, borrow_date)
                VALUES (?, ?, ?)
            ''', (book_id, member_id, borrow_date))
            
            # Update book availability
            cursor.execute('''
                UPDATE books SET available = available - 1
                WHERE book_id = ?
            ''', (book_id,))
            
            conn.commit()
            print("Book borrowed successfully!")
        else:
            print("Book is not available!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def return_book(book_id, member_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        return_date = datetime.date.today()
        cursor.execute('''
            UPDATE borrowings 
            SET return_date = ?
            WHERE book_id = ? AND member_id = ? AND return_date IS NULL
        ''', (return_date, book_id, member_id))
        
        cursor.execute('''
            UPDATE books 
            SET available = available + 1
            WHERE book_id = ?
        ''', (book_id,))
        
        conn.commit()
        print("Book returned successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def main_menu():
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            quantity = int(input("Enter quantity: "))
            add_book(title, author, isbn, quantity)
            
        elif choice == "2":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            phone = input("Enter member phone: ")
            add_member(name, email, phone)
            
        elif choice == "3":
            book_id = int(input("Enter book ID: "))
            member_id = int(input("Enter member ID: "))
            borrow_book(book_id, member_id)
            
        elif choice == "4":
            book_id = int(input("Enter book ID: "))
            member_id = int(input("Enter member ID: "))
            return_book(book_id, member_id)
            
        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()