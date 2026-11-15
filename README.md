# Internship Tracker

A Django-based web application that helps users manage and track their internship and job applications in one place.

Users can create an account, add applications, update application details, track application statuses, and view dashboard statistics.

## Features

- User registration, login, and logout
- Add, edit, and delete job or internship applications
- Dashboard displaying application statistics
- Track application statuses such as Applied, Interview, Selected, and Rejected
- Search applications by company or job role
- Filter applications by status
- Pagination for application records
- User-specific application management

## Technology Stack

**Backend:** Python, Django  
**Frontend:** HTML, CSS, Bootstrap  
**Database:** MySQL  
**Authentication:** Django Authentication System  
**ORM:** Django ORM  
**Version Control:** Git and GitHub

## Project Structure

```text
Internship-Tracker/
│
├── accounts/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── applications/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
│
├── tracker/
│   └── settings/
│       ├── common.py
│       ├── dev.py
│       └── prod.py
│
├── templates/
├── static/
│   └── css/
├── api/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/harshitha-s-14/Internship-Tracker.git
cd Internship-Tracker
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the MySQL database

Open MySQL and execute:

```sql
CREATE DATABASE tracker;
```

### 5. Configure environment variables

Create a `.env` file in the project root directory.

Add your own local configuration:

```env
SECRET_KEY=your_django_secret_key
DB_PASSWORD=your_mysql_password
```

Do not upload your `.env` file or share your passwords publicly.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Learning Outcomes

- Developed a full-stack web application using Django.
- Implemented user authentication and authorization.
- Performed database operations using Django ORM and MySQL.
- Built CRUD functionality for managing applications.
- Implemented search, filtering, and dashboard statistics.
- Used Git and GitHub for version control.