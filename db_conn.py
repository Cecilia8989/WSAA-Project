import mysql.connector
from config import DBConfigSQL as cfg
import json

database = "employees_management"

logins_table = 'authentication_logins'
employee_table = "employees"

attkeys_employee=['id','first_name','last_name', "employee_id", "market"]
attkeys_logins=['id', 'username','first_name','last_name', "password"]

class database_connection:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''

    def __init__(self):
        self.host=       cfg.HOST
        self.user=       cfg.USER
        self.password=   cfg.PASSWORD
        self.database=   database

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
            
    def getAll(self, table, attkeys):
        cursor = self.getcursor()
        sql = f"SELECT * FROM `{table}`"  
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(attkeys, result))

        self.closeAll()
        return returnArray
    
    def convertToDictionary(self, attkeys, resultLine):
        list = {}
        currentkey = 0
        for attrib in resultLine:
            list[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return list
    
    
    
    def check_unique_username(self, username):
        cursor = self.getcursor()
        sql = f"SELECT * FROM authentication_logins WHERE username = '{username}'"
        cursor.execute(sql,)
        results = cursor.fetchall()
        self.closeAll()
        return results
    
    def check_unique_employee_id(self, employee_id):
        cursor = self.getcursor()
        sql = f"SELECT * FROM employees WHERE employee_id = '{employee_id}'"
        cursor.execute(sql,)
        results = cursor.fetchone()
        self.closeAll()
        if results:
            return True
        else:
            False

    def createNewEmployee(self, employee):
        cursor = self.getcursor()
        sql = "INSERT INTO employees (first_name, last_name, employee_id, market) VALUES (%s, %s, %s, %s)"
        values = (employee.get("first_name"), employee.get("last_name"), employee.get("employee_id"), employee.get("market"))
        print(values)
        cursor.execute(sql, values)
        self.connection.commit()  
        newid = cursor.lastrowid
        employee["id"] = newid
        self.closeAll()
        return employee
    
    def create_new_login(self, user):
        cursor = self.getcursor()
        sql = "INSERT INTO authentication_logins (username, first_name, last_name, password) VALUES (%s, %s, %s, %s)"
        values = (user.get("username"), user.get("first_name"), user.get("last_name"), user.get("password"))
        cursor.execute(sql, values)
        self.connection.commit()  
        newid = cursor.lastrowid
        user["id"] = newid
        self.closeAll()
        return user

    
    
    def get_user_by_username(self, username):
        cursor = self.getcursor()
        sql = f"SELECT * FROM authentication_logins WHERE username = '{username}'"
        cursor.execute(sql)
        result = cursor.fetchone()  # Assuming only one user should be returned
        self.closeAll()

        if result:
            return self.convertToDictionary(attkeys_logins, result)
        else:
            return None

    def get_user_by_emp_id(self, employee_id):  
        cursor = self.getcursor()
        sql = f"SELECT * FROM employee WHERE employee_id = {employee_id}"
        cursor.execute(sql)
        result = cursor.fetchall()  # Assuming only one user should be returned
        self.closeAll()

        if result:
            return self.convertToDictionary(attkeys_employee, result)
        else:
            return None

    def update_Employee(self, id, employee):
        cursor = self.getcursor()
        sql="update employee set first_name= %s,last_name=%s, employee_id=%s, market=%s where id = %s"
        print(f"update employee {employee}")
        values = (employee.get("first_name"), employee.get("last_name"), employee.get("employee_id"),employee.get("market"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
    
    
# Instantiate the database_connection class
db_conn = database_connection()

result = db_conn.check_unique_employee_id('asdfasD78#')
print(result)