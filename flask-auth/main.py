from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import secrets

# Initialize the Flask application
app = Flask(__name__)

# Configure a secret key for the Flask application, used for sessions and security
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Use a secure random key

# Configure the database URI. SQLite is used here with a database file named 'users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Initialize Flask-Login with the Flask app
login_manager = LoginManager()
login_manager.init_app(app)

# Function to load a user based on user_id from the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Fetch user from the database using the user_id

# Define the User model for the database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the user
    email = db.Column(db.String(100), unique=True)  # User email, should be unique
    password = db.Column(db.String(100))  # User password hash
    name = db.Column(db.String(1000))  # User's full name

# Create the database tables for the User model
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    # Render the index.html template and pass the logged_in status to it
    return render_template("index.html", logged_in=current_user.is_authenticated)

# Route for user registration
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()  # Check if email is already registered

        if user:
            flash("You've already signed up with that email, log in instead!")  # Show a flash message if email exists
            return redirect(url_for('login'))  # Redirect to login page if email exists

        # Hash the password with a salt
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        # Create a new user instance
        new_user = User(
            email=request.form.get('email'),
            password=hash_and_salted_password,
            name=request.form.get('name'),
        )
        db.session.add(new_user)  # Add the new user to the database
        db.session.commit()  # Commit changes to the database
        login_user(new_user)  # Log in the new user
        return redirect(url_for("secrets"))  # Redirect to the secrets page

    # Render the registration page
    return render_template("register.html", logged_in=current_user.is_authenticated)

# Route for user login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()  # Fetch user by email
        if not user:
            flash("That email does not exist, please try again.")  # Show flash message if email not found
            return redirect(url_for('login'))  # Redirect to login page if email does not exist
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')  # Show flash message if password is incorrect
            return redirect(url_for('login'))  # Redirect to login page if password is incorrect
        else:
            login_user(user)  # Log in the user
            return redirect(url_for('secrets'))  # Redirect to the secrets page

    # Render the login page
    return render_template("login.html", logged_in=current_user.is_authenticated)

# Route for the secrets page, accessible only to logged-in users
@app.route('/secrets')
@login_required
def secrets():
    # Render the secrets.html template and pass the user's name and logged_in status
    return render_template("secrets.html", name=current_user.name, logged_in=True)

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Log out the current user
    return redirect(url_for('home'))  # Redirect to the home page

# Route for downloading a file, accessible only to logged-in users
@app.route('/download')
@login_required
def download():
    # Serve the file 'cheat_sheet.pdf' from the 'static/files' directory
    return send_from_directory('static/files', 'cheat_sheet.pdf')

# Run the application in debug mode
if __name__ == "__main__":
    app.run(debug=True)








