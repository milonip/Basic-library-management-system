import sqlite3

def create_connection():
    conn = sqlite3.connect('library.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Create Books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            quantity INTEGER NOT NULL,
            available INTEGER NOT NULL
        )
    ''')

    # Create Members table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

    # Create Borrowings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowings (
            borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            member_id INTEGER,
            borrow_date DATE NOT NULL,
            return_date DATE,
            FOREIGN KEY (book_id) REFERENCES books (book_id),
            FOREIGN KEY (member_id) REFERENCES members (member_id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()