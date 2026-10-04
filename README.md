# Manga Reader

A manga reading application with a React frontend and Django backend/API.

## Technologies

React 19, Create React App, JavaScript, Python, and Django.

## Setup and run

Start the backend:

```bash
cd backend
python -m venv .venv
.venv/Scripts/activate
python -m pip install django
python manage.py migrate
python manage.py runserver
```

Start the frontend in another terminal:

```bash
cd frontend
npm install
npm start
```

The backend currently has no requirements file; install any additional dependencies required by the API as needed.
