# Student Management System

A web-based Student Management System built with Django, enabling efficient management of student data, including registration, editing, deletion, search/filtering, and basic administration. The project uses SQLite as the database backend and provides CRUD operations via a simple interface.

## Features

- Add, edit, and delete student records
- Search and filter students by name
- Enforce age and email constraints on records
- View student lists with detailed info
- Simple authentication and admin features via Django Admin
- Extensible by adding more fields/models via Django ORM

## Tech Stack

- **Backend:** Python (Django 6.0.5)
- **Frontend:** HTML (Django Templates), CSS (static), basic Bootstrap (optional, add to static if desired)
- **Database:** SQLite (default Django backend)
- **Other:** Django ORM, Django Admin

## Getting Started

### Prerequisites

- Python 3.x installed
- pip (Python package manager)
- (Optional but recommended) virtualenv

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Husewnberg87/student-management-system.git
   cd student-management-system
   ```

2. **Create and activate a Python virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install Django
   ```

4. **Database setup and migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser for the Django admin site (optional but recommended):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   The application will be available at [http://localhost:8000](http://localhost:8000).

## Usage

- Navigate to `/` to see the student list, and use the **Add**, **Edit**, or **Delete** actions.
- Use the search box to filter students by name.
- Use [Django Admin](http://localhost:8000/admin/) for advanced management.

## Project Structure

```
student-management-system/
├── config/                 # Django settings, urls, wsgi/asgi, etc.
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── students/               # Main application for student management
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   └── students/
│   │       ├── base.html
│   │       ├── list.html
│   │       ├── add.html
│   │       └── edit.html
│   └── static/
├── db.sqlite3              # SQLite database (auto-created after migration)
├── manage.py
└── README.md
```

## Main Modules and Code Structure

### Models (`students/models.py`)
Defines the `Student` model with fields:
- `name` (CharField, max 100)
- `age` (IntegerField, 16-60 validation)
- `department` (CharField, max 100)
- `email` (EmailField)

### Views (`students/views.py`)
- `student_list`: displays/searches students
- `student_add`: adds a new student
- `student_edit`: edits an existing student
- `student_delete`: deletes a student

### URLs (`config/urls.py`, `students/urls.py`)
- Root routes are handled by `students`
- CRUD paths at `/`, `/add/`, `/edit/<id>/`, `/delete/<id>/`
- Admin at `/admin/`

### Templates
- All templates inherit from `base.html`
- Main templates: `list.html`, `add.html`, `edit.html` (see `students/templates/students/`)

## Contributing

1. Fork this repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a Pull Request

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Python](https://python.org/)
- [Django](https://djangoproject.com)
