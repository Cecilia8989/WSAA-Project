# Importing required modules
from flask import Flask, render_template, request, flash, jsonify, abort, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from db_conn import db_conn as msd
from config import SecretKey as sk
from werkzeug.security import generate_password_hash, check_password_hash

# Define tables and attributes
logins_table = 'authentication_logins'
employee_table = "employees"
attkeys_employee = ['id', 'first_name', 'last_name', "employee_id", "market"]
attkeys_logins = ['id', 'username', 'first_name', 'last_name', "password"]

# Initialize Flask app
app = Flask(__name__, static_url_path='', static_folder='.')
app.config['SECRET_KEY'] = sk.KEY  # Setting secret key for sessions
app.config['SESSION_COOKIE_SAMESITE'] = 'None'  # Setting SameSite attribute for session cookies
app.config['SESSION_COOKIE_SECURE'] = True  # Ensuring session cookies are secure

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

# Route for home
@app.route('/')
def index():
    return render_template('home.html', user=current_user)  

# Route for logging out
@app.route('/logout')
def logout():
    # Check if the current user is authenticated
    if current_user.is_authenticated:
        logout_user()  # Log out the user
        flash("You have been logged out")  
    # Redirect to the login page
    return redirect(url_for('login'))

# Route for managing employees)
@app.route('/employees', methods=['GET', 'POST', 'PUT', 'DELETE'])
# Redirect to the login page
# Ensure login is required to access this route
@login_required  
def employees():
    if request.method == 'GET':
        # Return all employees as JSON
        return jsonify(msd.getAll(employee_table, attkeys_employee))  
    
    elif request.method == 'POST':
        # Extract employee data from JSON request
        employee = {
            "first_name": request.json['first_name'],
            "last_name": request.json['last_name'],
            "employee_id": request.json['employee_id'],
            "market": request.json['market'],
        }
        # Create a new employee
        added_employee = msd.createNewEmployee(employee)  
        # Return the newly created employee with HTTP status 201 (Created)
        return jsonify(added_employee), 201 

    if request.method == 'PUT':
        # Extract employee data from JSON request for updating
        employee = {
            "id": request.json['id'],
            "first_name": request.json['first_name'],
            "last_name": request.json['last_name'],
            "employee_id": request.json['employee_id'],
            "market": request.json['market'],
        }
        
        # Find the employee in the database by ID
        found_employee = msd.find_by_id(employee["id"])
        
        # If employee not found, abort with 404 (Not Found)
        if not found_employee:
            abort(404)
        
        # Update the found employee with the new data
        updated_employee = msd.update_employee(found_employee['id'], employee)
        
        # Flash a success message indicating the update
        flash(f"Employee with ID = {found_employee['id']} - First Name = {employee['first_name']} updated", category='success')
        # Return the updated employee data as JSON
        return jsonify(updated_employee) 

    elif request.method == 'DELETE':
        # Check if JSON data is present in the request
        if not request.json:
            abort(400) 
            
        # Get the employee ID from the JSON data
        found_employee_id = request.json.get('id')
        
        # Check if the employee ID is provided
        if not found_employee_id:
            abort(400)  
        
               
        # Delete the employee from the database
        msd.delete_employee(found_employee_id)
        
        # Flash a success message indicating the deletion of the employee
        flash(f"Employee with ID = {found_employee_id} deleted", category='success')
        # Return a JSON response indicating successful deletion
        return jsonify({"done":True})

    # Redirect to the updateDB route if the request method is neither PUT nor DELETE
    return redirect(url_for('updateDB'))  

 
        
@app.route('/show_employees')
def showDB():
    return render_template('showDB.html', user=current_user)

@app.route('/update_DB')
@login_required
def updateDB():
    if not current_user.is_authenticated:
        flash('Authentication required.', category='error')
        return redirect(url_for('index'))
    return render_template('update_DB copy.html', user=current_user)

@app.route('/create_employees', methods=['GET', 'POST'])
@login_required
def create_employees():
    if not current_user.is_authenticated:
        flash('Authentication required.', category='error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        employee_id = request.form.get('employee_id')
        result = msd.check_unique_employee_id(employee_id)
        
        if result == True:
            flash(f"Employee ID {employee_id} already exists. Please choose a different one.", category="error")
            return render_template('create_employee.html', user=current_user)
        
        flash('Employee created successfully.', category='success')

    return render_template('create_employee.html', user=current_user)

@app.route('/update_employee', methods=['GET', 'POST', 'PUT'])
def update_employee():
    # Ottieni i dati dell'impiegato dalla richiesta
    return render_template('update_employee.html')

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
        user.id = user_data['id']
        login_user(user, remember=True)

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
            return render_template('sign_up.html')
        
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
            new_user = {'username': username,
                        'first_name': first_name,
                        'last_name': last_name,
                        'password': password}
            msd.create_new_login(new_user)
            flash(f"User {username} successfully created", category='success')
            return redirect(url_for('login'))
        
    return render_template('sign_up.html', user=current_user)

if __name__ == '__main__':
    app.run(debug=True)