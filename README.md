Your README content goes here

# Django Authentication System

This project is a user authentication system built using Django. It includes functionalities for user sign up, login, password management, and a user dashboard with restricted access.

## Features

- **Login Page**: Users can log in with either their username or email and password.
- **Sign Up Page**: Users can register by providing a username, email, password, and confirm password.
- **Forgot Password**: Allows users to reset their password by entering their email.
- **Change Password**: Authenticated users can change their password after logging in.
- **Dashboard**: Displays a personalized greeting and links to Profile and Change Password pages.
- **Profile Page**: Displays user details such as username, email, and account timestamps.


## Installation

1. Clone the repository:git@github.com:Vaibhavkadam304/secure-login-system.git
   ```bash
   git clone 
   cd authsystem
Set up a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


python manage.py migrate
Create a superuser (optional for accessing the admin):

python manage.py createsuperuser
Start the Django development server:


python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/ to access the application.

Pages Overview
Login Page: Accessible via /login/.
Sign Up Page: Accessible via /signup/.
Forgot Password Page: Accessible via /forgot-password/.
Change Password Page: Accessible via /change-password/ (requires login).
Dashboard Page: Accessible via /dashboard/ (requires login).
Profile Page: Accessible via /profile/ (requires login).


