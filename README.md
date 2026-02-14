# Library Management System

A simple Django web application for managing and searching books in a library.

## Features

- **Search Books**: Search by title, author, or ISBN
- **Filter**: Filter books by category and availability status
- **Sort**: Sort by title, author, category, or date added
- **Pagination**: Browse books with pagination (12 per page)

## Installation

1. Install dependencies:
```bash
pip install django
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Start the development server:
```bash
python manage.py runserver
```

4. Open your browser and navigate to `http://127.0.0.1:8000/`

## Book Model

Each book has the following fields:
- Title
- Author
- Category
- ISBN
- Publication Year
- Status (Available/Issued)
- Added Date

## Tech Stack

- **Framework**: Django 4.2
- **Database**: SQLite
- **Language**: Python
