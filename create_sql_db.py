# Author: Cecilia Pastore
# Name: create_sql.py
# Subject: Web Service and application

# This script connects to a MySQL and create if needed the employees_management managements database, 
# creates necessary tables if they don't exist,and populates them with sample data. 
# It also includes methods to execute SQL queries, create a database, create tables, empty tables, and reset data.

# Importing MySQL Connector module
import mysql.connector
# Importing database configuration from config.py
from config import DBConfigSQL as cfg  

# Setting the name of the database
database = "employees_management"

# Database Connection Class
class DatabaseConnection:
    # Constructor
    def __init__(self):
        # Initializing database connection parameters
        self.host = cfg.HOST
        self.user = cfg.USER
        self.password = cfg.PASSWORD
        self.database = database
        self.connection = None
        self.cursor = None

    # Method to establish database connection
    def connect(self):
        try:
            # Attempting to establish a connection
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            # Creating a cursor object for executing SQL queries
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print("Error:", err)

    # Method to close the database connection
    def close(self):
        # Checking if cursor and connection are not None before closing
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    # Method to execute a SQL query
    def execute_query(self, sql_query):
        try:
            # Establishing a database connection
            self.connect()
            # Executing the SQL query using the cursor
            self.cursor.execute(sql_query)
            # Committing the changes to the database
            self.connection.commit()
        except mysql.connector.Error as err:
            # Handling any errors that occur during query execution
            print("Error executing query:", err)
        finally:
            # Closing the database connection
            self.close()

    # Method to create the database if it doesn't exist
    def create_db(self):
        try:
            # Establishing a connection to the MySQL server
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
            )
            # Creating a cursor object for executing SQL queries
            cursor = connection.cursor()
            # SQL query to create the database if it doesn't already exist
            sql = f"CREATE DATABASE IF NOT EXISTS {self.database};"
            cursor.execute(sql)
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            # Closing the database connection
            self.close()
            
    # Method to create the 'authentication_logins' table if not exist
    def create_authentication_logins_table(self):
        try:
            # Establishing a database connection
            self.connect()
            # SQL query to create the 'authentication_logins' table if it doesn't already exist
            sql = """
            CREATE TABLE IF NOT EXISTS authentication_logins (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                password VARCHAR(50)
            );
            """
            # Executing the SQL query using the cursor
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            # Closing the database connection
            self.close()
            print("Authentication logins table already exists or has been created.")
    
    # Method to create the 'employees' table if not exist
    def create_employees_table(self):
        try:
            self.connect()
            # SQL query to create the 'employees' table if it doesn't already exist
            sql = """
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                employee_id VARCHAR(50) UNIQUE,
                market VARCHAR(50)
            );
            """
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            self.close()
            print("Employees table already exists or has been created.")

    # Method to empty a table
    def empty_table(self, table_name):
        try:
            self.connect()
            # SQL query to delete all records from the specified table
            sql = f"DELETE FROM {table_name};"
            self.cursor.execute(sql)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            self.close()

    # Method to reset employee data
    def reset_data_employees(self):
        try:
            self.connect()
            # SQL query to retrieve any records from the 'employees' table
            sql = f"SELECT * FROM employees;"
            self.cursor.execute(sql)
            # Fetching the first result
            result = self.cursor.fetchone()
            # If there are records in the table, empty it
            if result:
                self.empty_table("employees") 
            # SQL query to insert sample employee data into the 'employees' table
            sql = """
            INSERT INTO employees (first_name, last_name, employee_id, market)
            VALUES
                ('John', 'Doe', 'EMP001', 'DE'),
                ('Jane', 'Smith', 'EMP002', 'IT'),
                ('Michael', 'Johnson', 'EMP003', 'FR'),
                ('Emily', 'Brown', 'EMP004', 'DE'),
                ('David', 'Wilson', 'EMP005', 'IT');
            """
            self.cursor.execute(sql)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            self.close()
            print("Employee data has been inserted/reset to the original state.")
            
    # Method to reset login data
    def reset_data_logins(self):
        try:
            self.connect()
            # SQL query to retrieve any records from the 'authentication_logins' table
            sql = f"SELECT * FROM authentication_logins;"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            # If there are records in the table, empty it
            if result:
                self.empty_table("authentication_logins") 
            # SQL query to insert sample login data into the 'authentication_logins' table
            sql = """
            INSERT INTO authentication_logins (username, first_name, last_name, password)
            VALUES
                ('user1', 'John', 'Doe', 'password1#'),
                ('user2', 'Jane', 'Smith', 'password2#'),
                ('user3', 'Michael', 'Johnson', 'password3#'),
                ('user4', 'Emily', 'Brown', 'password4#'),
                ('user5', 'David', 'Wilson', 'password5#');
            """
            self.cursor.execute(sql)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            self.close()
            print("Login data has been inserted/reset into the authentication logins table.")
            
# Entry point of the script
if __name__ == "__main__":
    # Creating a DatabaseConnection object
    db_conn = DatabaseConnection()

    # Create the database if it doesn't exist
    if db_conn.create_db(): 
        print("Database created or already exists.")

    # Create the 'authentication_logins' table
    db_conn.create_authentication_logins_table()
    # Create the 'employees' table
    db_conn.create_employees_table()
    # Reset employee data
    db_conn.reset_data_employees()
    # Reset login data
    db_conn.reset_data_logins()