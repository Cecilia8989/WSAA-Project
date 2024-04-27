import mysql.connector
from config import DBConfigSQL as cfg
import json

database = "employee_management"

logins_table = 'authentication_logins'
employee_table = "employees"

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
            
    def getAll(self, table):
        cursor = self.getcursor()
        sql = f"SELECT * FROM `{table}`"  # Backticks are used to properly escape the table name
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        self.closeAll()
        return returnArray
    
    def convertToDictionary(self, resultLine):
        attkeys=['id','First Name','Second Name', "Employee ID"]
        employee = {}
        currentkey = 0
        for attrib in resultLine:
            employee[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return employee
    
    def checkUniqueEmployeeID(self, employee_id):
        cursor = self.get_cursor()
        sql = "Select %s from %s"
        values = (employee_id, employee_table)
        cursor.execute(sql, values)
        results = cursor.fetchall()
        return results
       
db_conn = database_connection()
