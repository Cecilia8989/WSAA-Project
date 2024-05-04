from flask import Flask, render_template, request, flash, jsonify, abort, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from db_conn import db_conn as msd
from config import SecretKey as sk
from werkzeug.security import generate_password_hash, check_password_hash
import sys

# Define tables and attributes
logins_table = 'authentication_logins'
employee_table = "employees"
attkeys_employee = ['id', 'first_name', 'last_name', "employee_id"]
attkeys_logins = ['id', 'username', 'first_name', 'last_name', "password"]

# Initialize Flask app
app = Flask(__name__, static_url_path='', static_folder='.')
app.config['SECRET_KEY'] = sk.KEY

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Set the login view for login_required decorator

# User class for Flask-Login
class User(UserMixin):
    pass

# User loader callback function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user

# Routes

@app.route('/')
def index():
    return render_template('home.html', user=current_user)

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("You have been logged out")
    return redirect(url_for('login'))

@app.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'GET':
        return msd.getAll(employee_table)
    elif request.method == 'POST':
        if not request.json:
            abort(400)
        employee = {
            "first_name": request.json['first_name'],
            "last_name": request.json['last_name'],
            "employee_id": request.json['employee_id'],
        }
        added_employee = msd.createNewEmployee(employee)
        return jsonify(added_employee)
        
@app.route('/show_employees')
def showDB():
    return render_template('showDB.html', user=current_user)

@app.route('/update_employees')
@login_required
def updateDB():
    if not current_user.is_authenticated:
        flash('Authentication required.', category='error')
        return redirect(url_for('login'))
    return render_template('update_DB.html', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user_data = msd.get_user_by_username(username)
        
        if not user_data:
            flash('Username not found', category='error')
            return render_template('login.html')
        
        if not user_data['password'] == password:
            flash('Incorrect password', 'error')
            return render_template('login.html')

        user = User()
        user.id = user_data['id']  # Set user ID
        login_user(user, remember=True)  # Log in the user

        flash('Login successful!', 'success')
        return redirect(url_for('index'))
    
    return render_template('login.html', user=current_user)

@app.route('/sign-up', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password1')
        password2 = request.form.get('password2')
        special_chars = ['$', '@', '#', '%']
        
        if msd.check_unique_username(username):
            flash("Username already exists. Please choose a different one.", category="error")
            return render_template('sign_up.html')  # Render the sign-up template again
        
        if password != password2:
            flash("Passwords do not match", category="error")
        elif len(password) < 6:
            flash("Password should be at least 6 characters long", category="error")
        elif len(password) > 20:
            flash("Password should not be greater than 20 characters", category="error")
        elif not any(char.isdigit() for char in password):
            flash("Password should have at least one numeral", category="error")
        elif not any(char.isupper() for char in password):
            flash("Password should have at least one uppercase letter", category="error")
        elif not any(char in special_chars for char in password):
            flash("Password should have at least one of the symbols $@#", category="error")
        else:
            hashed_password = generate_password_hash(password)  # Hash the password
            new_user = {'username': username,
                        'first_name': first_name,
                        'last_name': last_name,
                        'password': hashed_password}
            msd.create_new_login(new_user)
            flash(f"User {username} successfully created", category='success')
            return redirect(url_for('index'))  # Redirect to the home page
        
    return render_template('sign_up.html', user=current_user)



if __name__ == '__main__':
    app.run(debug=True)