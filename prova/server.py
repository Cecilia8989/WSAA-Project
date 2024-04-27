from flask import Flask, Blueprint, render_template, request, flash, jsonify
from db_conn import db_conn as msd
from config import SecretKey as sk

app = Flask(__name__, static_url_path='', static_folder='.')
app.config['SECRET_KEY'] = sk.KEY

#app = Flask(__name__)
logins_table = 'authentication_logins'
employee_table = "employees"


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign-up')
def SignUp():
    return render_template('sign_up.html')

@app.route('/logout')
def logout():
    return render_template('home.html')

@app.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'GET':
        return msd.getAll(employee_table)   
    elif request.method == 'POST':
        employee_id = request.form.get('employee_id')
        if msd.checkUniqueEmployeeID(employee_id):
            flash("Username already exists. Please choose a different one.", category="error")
            return render_template('update_DB.html')  # Ritorna il template per consentire all'utente di correggere l'errore
        else:
            # Aggiungi qui la logica per creare un nuovo impiegato nel database
            flash("Employee created successfully")
            return render_template('update_DB.html')  # Ritorna il template per informare l'utente che l'impiegato è stato creato
       

@app.route('/show_employees')
def showDB():
    return render_template('showDB.html')

@app.route('/update_employees')
def updateDB():
    return render_template('update_DB.html')

if __name__ == '__main__' :
    app.run(debug= True)