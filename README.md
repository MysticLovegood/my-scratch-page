# Flask Portfolio & Comment Web App

This is a simple Flask-based web application created as part of a learning project. It features a personal portfolio page and a comment section where users can submit and view comments. It is designed to demonstrate full-stack development skills, including Python backend, HTML templating, database integration, user authentication, and basic security practices. The app is deployed on [PythonAnywhere](https://www.pythonanywhere.com/).

---

## Features

- Personalised portfolio page
- Comment section to add and view comments
- Hosted using PythonAnywhere 
- Comments stored in MySQL database
- Login page with username and password form

---

## Project Structure

```
my-scratch-page/
├── app.py                    # Main Flask application
├── models.py                 # Database models (User, Comment)
├── README.md                 # Project description and setup guide
├── config.py                 # Configurations like secret key, database URI
├── venv/                     # Python virtual environment
├── static/                   # Static files (CSS, JS, images)
│   └── style.css
│   └── photo.jpg     
├── templates/                # HTML templates
│   ├── index.html            # Scratch page (comment section)
│   ├── intro.html            # Introduction page
│   ├── layout.html           # Base layout
│   └── login.html            # Login form
└
```

---

## Getting Started

### Prerequisites

- Python 3.x
- Git
- Flask – Web framework
- Flask-SQLAlchemy – ORM for database handling
- Werkzeug – Password hashing and authentication support
- Flask-Login – User session management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MysticLovegood/my-scratch-page.git
   cd my-scratch-page
   ```

2. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv/Scripts/activate
   ```

3. Install dependencies:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Login pymysql
   ```

4. Run the Flask app:
   ```bash
   flask run
   ```

5. Visit `http://127.0.0.1:5000` in your browser.

---

## Deployment on PythonAnywhere

1. Create an account on [PythonAnywhere](https://www.pythonanywhere.com/)
2. Upload your project or clone it using Git
3. Set up a new Flask app from the dashboard
4. Set up a MySQL database from the dashboard
5. Point the WSGI file to your `app.py`
6. Reload your web app to apply changes

---

## Learning Objectives

- Use Flask to build a web app
- Apply HTML templating (Jinja2) and CSS styling
- Practice version control using Git
- Deploy a live web app using PythonAnywhere
- Integrate a backend database with MySQL
- Apply basic security features to secure a web app

---