import mysql.connector
from config import DBConfigSQL as cfg

database = "employees_management"

class DatabaseConnection:
    def __init__(self):
        self.host = cfg.HOST
        self.user = cfg.USER
        self.password = cfg.PASSWORD
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print("Error:", err)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, sql_query):
        try:
            self.connect()
            self.cursor.execute(sql_query)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error executing query:", err)
        finally:
            self.close()

    def create_db(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
            )
            cursor = connection.cursor()
            sql = f"CREATE DATABASE IF NOT EXISTS {self.database};"  
            cursor.execute(sql)
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False
        finally:
            connection.close()

    def create_authentication_logins_table(self):
        try:
            self.connect()
            sql = """
            CREATE TABLE IF NOT EXISTS authentication_logins (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                password VARCHAR(50)
            );
            """
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            self.close()
            print("Authentication logins already existed/created.")

    def create_employees_table(self):
        try:
            self.connect()
            sql = """
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                employee_id VARCHAR(20) UNIQUE,
                market VARCHAR(10)
            );
            """
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            self.close()
            print("Employees already existed/created.")
    
    def empty_table(self, table_name):
        try:
            self.connect()
            sql = f"DELETE FROM {table_name};"
            self.cursor.execute(sql)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            self.close()

    def reset_data_employees(self):
        try:
            self.connect()
            sql = f"SELECT * FROM employees;"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            if result:  # Check if there are any records in the table
                self.empty_table("employees")  # Empty the table
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
            print("Employee data insert/reset to the original")
            


    def reset_data_logins(self):
        try:
            self.connect()
            sql = f"SELECT * FROM authentication_logins;"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            if result:  # Check if there are any records in the table
                self.empty_table("authentication_logins")  # Empty the table
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
            print("Login data insertion /reset into authentication logins table.")

if __name__ == "__main__":
    db_conn = DatabaseConnection()

    if db_conn.create_db(): 
        print("Database created or already existing.")

    db_conn.create_authentication_logins_table()
    db_conn.create_employees_table()
    db_conn.reset_data_employees()
    db_conn.reset_data_logins()