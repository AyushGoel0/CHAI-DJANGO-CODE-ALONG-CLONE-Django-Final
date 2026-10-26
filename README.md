# CHAI-DJANGO-CODE-ALONG-CLONE-Django-Final

Final Django project from the **Chai aur Code Django playlist**.

Playlist reference:  
https://www.youtube.com/watch?v=j6szNSzw4BU&list=PLu71SKxNbfoDOf-6vAcKmazT92uLnWAgy&index=1&pp=iAQB

---

## Overview

This project is a small tweet application built with Django. Users can register
and log in, publish tweets with optional photos, view the tweet timeline, and
edit or delete their own tweets.

---

## Features

- User registration, login, and logout
- Tweet creation with text up to 240 characters
- Optional image uploads for tweets
- Timeline ordered by newest tweets first
- Edit and delete permissions limited to the tweet owner
- Django admin interface for managing tweets
- SQLite database for local development
- Bootstrap-based templates

---

## Local Setup (Windows PowerShell)

Clone the repository and move into the project directory:

```powershell
git clone https://github.com/AyushGoel0/CHAI-DJANGO-CODE-ALONG-CLONE-Django-Final.git
cd CHAI-DJANGO-CODE-ALONG-CLONE-Django-Final
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Apply database migrations:

```powershell
python manage.py migrate
```

Start the development server:

```powershell
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/tweet/
```

---

## Useful URLs

| Page | URL |
| --- | --- |
| Tweet timeline | `/tweet/` |
| Create a tweet | `/tweet/create/` |
| Register | `/tweet/register/` |
| Login | `/accounts/login/` |
| Django admin | `/admin/` |

To access the admin site, create an administrator account:

```powershell
python manage.py createsuperuser
```

---

## Project Structure

```text
config/                 Django project configuration
media/photos/           Uploaded tweet images
templates/              Shared and authentication templates
tweet/                  Tweet application
  migrations/           Database migrations
  templates/            Tweet-specific templates
  forms.py              Tweet and registration forms
  models.py             Tweet database model
  urls.py               Tweet URL routes
  views.py              Tweet and authentication views
db.sqlite3              Local SQLite database
manage.py               Django management utility
requirements.txt        Python dependency snapshot
```

---

## Dependencies

- Python
- Django 6.1.2
- Pillow 13.0.0
- SQLite

The complete dependency list is maintained in `requirements.txt`.

---

## Notes

- The project is configured for local development with `DEBUG = True`.
- Uploaded media is stored in `media/photos/`.
- The default database is the checked-in SQLite file `db.sqlite3`.
- The project uses the `config` Django settings module.

---

## Progress Tracker

- [x] Repository created
- [x] Django project configured
- [x] Tweet application added
- [x] SQLite database configured
- [x] Tweet creation, editing, and deletion
- [x] User registration and authentication
- [x] Image upload support
- [x] Templates and navigation added
- [x] Dependency snapshot saved in `requirements.txt`

---

## Author

Maintained by **@AyushGoel0**
