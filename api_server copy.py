from flask import Flask, Blueprint, render_template, request, flash, jsonify, abort, redirect, url_for
from db_conn import db_conn as msd
from config import SecretKey as sk


app = Flask(__name__, static_url_path='', static_folder='.')
app.config['SECRET_KEY'] = sk.KEY

logins_table = 'authentication_logins'
employee_table = "employees"

attkeys_employee=['id','first_name','last_name', "employee_id"]
attkeys_logins=['id', 'username','first_name','last_name', "password"]


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/logout')
def logout():
    return render_template('home.html')

@app.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'GET':
        return msd.getAll(employee_table)
    elif request.method == 'POST':
        #employee_id = request.form.get('employee_id')
        #if msd.checkUniqueID(employee_table, employee_id):
        #    flash("Username already exists. Please choose a different one.", category="error")
        #    return render_template('update_DB.html')  # Ritorna il template per consentire all'utente di correggere l'errore
        #else:
        #    # Aggiungi qui la logica per creare un nuovo impiegato nel database
        #    flash("Employee created successfully")
        #    return render_template('update_DB.html')  # Ritorna il template per informare l'utente che l'impiegato è stato creato
        if not request.json:
            abort(400)
        employee = {
            "first_name": request.json['first_name'],
            "last_name": request.json['last_name'],
            "employee_id": request.json['employee_id'],
        }
        addedemployee = msd.createNewEmployee(employee)
        return jsonify(addedemployee)
        
@app.route('/users', methods=['GET', 'POST'])
def users_list():
    if request.method == 'GET':
        return msd.getAll(logins_table, attkeys_logins)
    elif request.method == 'POST':
        if not request.json:
            abort(400)
                   
        user = {
            "username": request.json['username'],
            "first_name": request.json['first_name'],
            "last_name": request.json['last_name'],
            "password": request.json['password1']
            }
        addedeuser = msd.create_new_login(user)
        return jsonify(addedeuser)

@app.route('/show_employees')
def showDB():
    return render_template('showDB.html')

@app.route('/update_employees')
def updateDB():
    return render_template('update_DB.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(password)
        
        if msd.check_username_exist(username):
            if msd.check_passwrod_match(username, password):
                flash("Username and password match")
            else:
                flash(f"Password incorrect for username {username}, Please try again")    
                return redirect(url_for('login'))
        else:
            flash(f"Username {username} don't exist. Please register")    
            return redirect(url_for('signin'))
        
    
    return render_template('login.html', boolean=True)

@app.route('/sign-up', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password1')
        password2 = request.form.get('password2')
        SpecialSym =['$', '@', '#', '%']
        
    
        # Check if the username already exists using the instance of database_connection
        if msd.check_unique_username(username):
            flash("Username already exists. Please choose a different one.", category="error")
            return render_template('sign_up copy.html')  # Render the sign-up template again
        
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
        elif not any(char in SpecialSym for char in password):
            flash("Password should have at least one of the symbols $@#", category="error")
        else:
            new_user = {'username': username,
                        'first_name': first_name,
                        'last_name': last_name,
                        'password': password}
            msd.create_new_login(new_user)
            flash(f" User {username} succesfully created", category='success')
            return redirect(url_for('index'))  # Redirect to the home page
        
    return render_template('sign_up copy.html')

if __name__ == '__main__' :
    app.run(debug= True)