import click
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Comment
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from dotenv import load_dotenv

# Initialize the Flask app and SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if current_user.is_authenticated:
            new_comment = Comment(text=request.form['comment'], user_id=current_user.id)
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash('Please log in to comment.', 'warning')
            return redirect(url_for('login'))
    comments = Comment.query.order_by(Comment.id.desc()).all()
    return render_template('index.html', comments=comments)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid login credentials.', 'danger')
    return render_template('login.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.cli.command("create-db")
def create_db():
    db.create_all()
    print("Database created.")

@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user(username, password):
    if not User.query.filter_by(username=username).first():
        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        print("User {username} created.")
    else:
        print("User {username} already exists.")

if __name__ == '__main__':
    app.run(debug=True)
