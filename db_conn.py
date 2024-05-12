# db_conn.py
# Author: Cecilia Pastore

# This script defines a class `database_connection` that provides methods for interacting with a MySQL database,
# including establishing a connection, executing SQL queries, CRUD operations, and specific tasks like checking unique usernames or employee IDs.
# It utilizes the MySQL Connector/Python library and a configuration file (`DBConfigSQL`) for connection parameters.

# Importing MySQL connector library
import mysql.connector  
# Importing database configuration
from config import DBConfigSQL as cfg  

# Setting the name of the database
database = "employees_management"  

# Variable to store the name of the authentication logins table
logins_table = 'authentication_logins'  
# Variable to store the name of the employees table
employee_table = "employees"  

# Attribute keys for the employees table
attkeys_employee=['id','first_name','last_name', "employee_id", "market"] 
# Attribute keys for the authentication logins table 
attkeys_logins=['id', 'username','first_name','last_name', "password"]  

class database_connection:
    # Initialize class attributes
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''

    def __init__(self):
        # Initializing database connection parameters store in the config file
        self.host=       cfg.HOST
        self.user=       cfg.USER
        self.password=   cfg.PASSWORD
        self.database=   database

    # Method to establish a database connection and get a cursor
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    # Method to close both connection and cursor
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
   
    # Method to fetch all records from a table        
    def getAll(self, table, attkeys):
        # Get a database cursor
        cursor = self.getcursor()
        # SQL query to fetch all records from the table
        sql = f"SELECT * FROM `{table}`"
        # Execute the SQL query  
        cursor.execute(sql)
        # Fetch all records
        results = cursor.fetchall()
        # Initialate and empty array
        returnArray = []
        # Iterate through each record 
        for result in results:
            #convert it into a dictionary using the convertToDictionary function
            returnArray.append(self.convertToDictionary(attkeys, result))

        # Close the connection and cursor
        self.closeAll()
        # Return the list of dictionaries containing fetched records
        return returnArray
    
     # Method to convert database records to dictionaries
    def convertToDictionary(self, attkeys, resultLine):
        # Initialize an empty dictionary
        list = {}
        # Initialize the current key as 0
        currentkey = 0
        # Iterate through each attribute in the record and assign it to the corresponding key
        for attrib in resultLine:
            list[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return list
    
    
    # Method to check if a username is unique
    def check_unique_username(self, username):
        cursor = self.getcursor()
        # SQL query to select records with the given usernam
        sql = f"SELECT * FROM authentication_logins WHERE username = '{username}'"
        cursor.execute(sql,)
        results = cursor.fetchall()
        self.closeAll()
        return results
    
    # Method to check if an employee ID is unique
    def check_unique_employee_id(self, employee_id):
        cursor = self.getcursor()
        # SQL query to select a record with the given employee ID
        sql = f"SELECT * FROM employees WHERE employee_id = '{employee_id}'"
        cursor.execute(sql,)
        results = cursor.fetchone()
        self.closeAll()
        # Return True if a record exists with the employee ID, False otherwise
        if results:
            return True
        else:
            False

    # Method to create a new employee record
    def createNewEmployee(self, employee):
        cursor = self.getcursor()
        # SQL query to insert a new employee record
        sql = "INSERT INTO employees (first_name, last_name, employee_id, market) VALUES (%s, %s, %s, %s)"
        # Values to be inserted into the query
        values = (employee.get("first_name"), employee.get("last_name"), employee.get("employee_id"), employee.get("market"))
        cursor.execute(sql, values)
        # Commit the changes to the database
        self.connection.commit() 
        # Get the ID of the newly inserted record 
        newid = cursor.lastrowid
        # Assign the new ID to the employee dictionary
        employee["id"] = newid
        self.closeAll()
        # Return the user dictionary containing the newly assigned ID
        return employee
    
    # Method to create a new login record
    def create_new_login(self, user):
        cursor = self.getcursor()
        # Construct the SQL query to insert a new login record
        sql = "INSERT INTO authentication_logins (username, first_name, last_name, password) VALUES (%s, %s, %s, %s)"
        values = (user.get("username"), user.get("first_name"), user.get("last_name"), user.get("password"))
        cursor.execute(sql, values)
        self.connection.commit()  
        # Get the ID of the newly inserted record 
        newid = cursor.lastrowid
        # Assign the new ID
        user["id"] = newid
        self.closeAll()
        # Return the user dictionary containing the newly assigned ID
        return user
   
    # Method to fetch a user record by username
    def get_user_by_username(self, username):
        cursor = self.getcursor()
        # Construct the SQL query to fetch a user record by username
        sql = f"SELECT * FROM authentication_logins WHERE username = '{username}'"
        cursor.execute(sql)
        # Fetch the first result (assuming only one user should be returned)
        result = cursor.fetchone()  
        self.closeAll()

        if result:
            # If a result is found, convert it to a dictionary using specified attribute keys
            return self.convertToDictionary(attkeys_logins, result)
        else:
            # If no result is found, return None
            return None

    # Method to fetch a user record by employee ID
    def get_user_by_emp_id(self, employee_id):  
        cursor = self.getcursor()
        # Construct the SQL query to fetch a user record by employee ID
        sql = f"SELECT * FROM employees WHERE employee_id = '{employee_id}'"
        cursor.execute(sql)
        # Fetch the first result (assuming only one user should be returned)
        result = cursor.fetchone()  
        self.closeAll()

        if result:
            # If a result is found, convert it to a dictionary using specified attribute keys
            return self.convertToDictionary(attkeys_employee, result)
        else:
            # If no result is found, return None
            return None

    # Method to fetch a record by ID
    def find_by_id(self, id):
        cursor = self.getcursor()
        # Construct the SQL query to fetch a user record by ID
        sql = f"SELECT * FROM employees WHERE id = {id}"
        cursor.execute(sql)
        result = cursor.fetchone()  # Assuming only one user should be returned
        self.closeAll()

        if result:
            # If a result is found, convert it to a dictionary using specified attribute keys
            return self.convertToDictionary(attkeys_employee, result)
        else:
            # If no result is found, return None
            return None

    # Method to update an employee record
    def update_employee(self, id, employee):
        cursor = self.getcursor()
        # Define the SQL update statement
        sql = "update employees set first_name= %s,last_name=%s, employee_id=%s, market=%s where id = %s"
        # Define the values to be updated
        values = (employee.get("first_name"), employee.get("last_name"), employee.get("employee_id"), employee.get("market"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    # Method to delete an employee record    
    def delete_employee(self, id):
        cursor = self.getcursor()
        # Define the SQL delete statement
        sql = f"delete from employees where id ='{id}'"
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()
    
    
# Instantiate the database_connection class
db_conn = database_connection()

