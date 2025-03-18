# 📚 Library Management System

A robust command-line based Library Management System that helps librarians manage books, members, and borrowing operations efficiently.

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features
- **Book Management**
  - Add new books with details (title, author, ISBN)
  - Track book quantity and availability

- **Member Management**
  - Register new library members
  - Store member contact information

- **Borrowing System**
  - Check out books to members
  - Return books and update inventory
  - Automatic availability tracking

## 🛠 Tech Stack
- Python 3.x
- SQLite3 Database
- Command Line Interface

## 📁 Project Structure

Library-management-system/

├── main.py                    # Main application file

├── database.py                # Database operations

├── library.db                 # SQLite database

└── README.md                  # Documentation

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/milonip/Basic-library-management-system.git
   cd Basic-library-management-system
   ```

2. Initialize Database
   
   ```bash
   python database.py
    ```
3. Run the Application
   
   ```bash
   python main.py
    ```

## 📖 Usage Guide

### Adding a New Book
Choice: 1
Title: The Great Gatsby
Author: F. Scott Fitzgerald
ISBN: 9780743273565
Quantity: 3
➜ Book added successfully!

### Registering a New Member
Choice: 2
Name: John Smith
Email: john.smith@email.com
Phone: 1234567890
➜ Member added successfully!

### Borrowing Process
Choice: 3
Book ID: 1
Member ID: 1
➜ Book borrowed successfully!

### Return Process

Choice: 4
Book ID: 1
Member ID: 1
➜ Book returned successfully!

## 🗄️ Database Schema

### Books Table
| Column    | Type    | Description          |
|-----------|---------|---------------------|
| book_id   | INTEGER | Primary Key         |
| title     | TEXT    | Book title          |
| author    | TEXT    | Author name         |
| isbn      | TEXT    | Unique ISBN         |
| quantity  | INTEGER | Total copies        |
| available | INTEGER | Available copies    |

### Members Table
| Column    | Type    | Description          |
|-----------|---------|---------------------|
| member_id | INTEGER | Primary Key         |
| name      | TEXT    | Member name         |
| email     | TEXT    | Unique email        |
| phone     | TEXT    | Contact number      |

### Borrowings Table
| Column      | Type    | Description          |
|-------------|---------|---------------------|
| borrow_id   | INTEGER | Primary Key         |
| book_id     | INTEGER | Foreign Key (Books) |
| member_id   | INTEGER | Foreign Key (Members)|
| borrow_date | DATE    | Checkout date       |
| return_date | DATE    | Return date         |

## 🚀 Future Enhancements
- Fine calculation system
- Book reservation feature
- Email notifications
- Search functionality
- Admin authentication
- Web interface

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
Developed with ❤️ by [Miloni Patel](https://github.com/milonip)
