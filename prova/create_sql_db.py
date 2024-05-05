import mysql.connector
from config import DBConfigSQL as cfg  # Assuming DBConfigSQL contains your database configuration

database = "datarepresentation"  # Set the database name to 'datarepresentation'

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

    def create_book_table(self):
        try:
            self.connect()
            sql = """
            CREATE TABLE IF NOT EXISTS book (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                price DECIMAL(10, 2)
            );
            """
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            self.close()
            print("Book table created/already existed.")

    def insert_books(self):
        try:
            self.connect()
            sql = """
            INSERT INTO book (title, author, price)
            VALUES
                ('Title 1', 'Author 1', 20.99),
                ('Title 2', 'Author 2', 15.49),
                ('Title 3', 'Author 3', 25.99),
                ('Title 4', 'Author 4', 18.75),
                ('Title 5', 'Author 5', 30.00);
            """
            self.cursor.execute(sql)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            self.close()
            print("Books inserted into the table.")

if __name__ == "__main__":
    db_conn = DatabaseConnection()

    if db_conn.create_db(): 
        print("Database created or already existing.")

    db_conn.create_book_table()
    db_conn.insert_books()