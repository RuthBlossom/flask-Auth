
# Flask Authentication App

This is a basic Flask application that provides user authentication functionality, including registration, login, and logout. The app uses Flask, Flask-Login, Flask-SQLAlchemy, and Bootstrap for styling. Users can register an account, log in, view a protected page, and log out.

![Flask Auth](https://github.com/user-attachments/assets/5b5844bc-faa2-443e-b05a-e218e85c9b35)
![flask Auth 2](https://github.com/user-attachments/assets/ceda8b6a-97d9-4a2e-b88c-6dd987ab83b6)
![flask Auth 3](https://github.com/user-attachments/assets/0fdd8365-9479-4066-a33b-d0835d3c8e3c)

## Features

- User registration with hashed passwords
- User login with authentication
- Protected route accessible only to logged-in users
- Logout functionality
- Downloadable file for authenticated users

## Installation

Follow these steps to set up and run the application:

1. **Clone the Repository:**


2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application:**

   ```bash
   python app.py
   ```

6. **Access the Application:**

   Open a web browser and go to `http://127.0.0.1:5000` to view the application.

## File Structure

- `app.py`: The main application file containing routes and logic.
- `templates/`: Directory containing HTML templates for rendering pages.
  - `base.html`: The base template providing the structure for other pages.
  - `index.html`: The homepage template with a login form.
  - `login.html`: The login page template.
  - `register.html`: The registration page template.
  - `secrets.html`: The protected page accessible only to logged-in users.
- `static/`: Directory containing static files like CSS and JavaScript.
  - `css/styles.css`: Custom stylesheet for additional styling.
- `requirements.txt`: File listing the required Python packages.

## Configuration

- **Database**: Uses SQLite to store user information in `users.db`.
- **Secret Key**: A secure random key is used for session management. It's generated dynamically using `secrets.token_hex(16)`.

## Usage

1. **Registration**: Go to `/register` to create a new account. Fill in your name, email, and password to sign up.
2. **Login**: Go to `/login` to log in with your email and password.
3. **Secrets**: After logging in, you'll be redirected to `/secrets`, a protected page.
4. **Logout**: Click the "Log Out" link to log out of your account.
5. **File Download**: An authenticated user can download a file from the `/download` route.

## Requirements

- Python 3.x
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Werkzeug
- Bootstrap (for styling)



### Notes:


- Update `[your email address](mailto:your-email@example.com)` with your actual contact email.
- The `requirements.txt` file should list the dependencies, such as Flask, Flask-Login, Flask-SQLAlchemy, and Werkzeug. If you don't have one, you can generate it using `pip freeze > requirements.txt`.

