# Healthcare Project

A simple Django web application for managing healthcare operations, including patient records, appointments, and user management.

---

## Project Structure
```
healthcare_project/
├─ manage.py
├─ requirements.txt
├─ healthcare/ # Django project settings
├─ core/ # Main app with models, views, templates
│ ├─ templates/
│ └─ migrations/
└─ media/ # Uploaded files (ignored by Git)
```

---

## Features

- User registration and login
- Patient management
- Doctor and hospital profiles
- Appointment booking
- Upload medical records
- Dashboard for users

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- Virtual environment tool (venv or virtualenv)

### Installation

# 1. Clone the repository
git clone <your-repo-url>  
cd healthcare_project

# 2. Create and activate a virtual environment
python -m venv venv

**Linux/macOS**: source venv/bin/activate  
**Windows**: source venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver

# 6. Open your browser at:
http://127.0.0.1:8000/  
http://127.0.0.1:8000/admin - Admin Page

---
**Configuration**

**Database**: The project uses SQLite by default (db.sqlite3), which is ignored by Git.

**Media** files: User-uploaded files are stored in the media/ folder (ignored by Git).

**Environment variables**: Store sensitive data (e.g., secret key) in a .env file.

---
**Git Ignore**

The `.gitignore` includes:

```
*.sqlite3
__pycache__/
*.py[cod]
env/
venv/
media/
staticfiles/
.env
.vscode/
.idea/
.DS_Store
Thumbs.db

```
