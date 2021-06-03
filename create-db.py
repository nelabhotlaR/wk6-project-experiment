# This is onetime script to create database and tables in mysql database
# Whenever required provide new database name and add new tables to create.
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Raghava10',
    auth_plugin='mysql_native_password',
    database = "wk6pay"
)

my_cursor = mydb.cursor()

# creating database
my_cursor.execute("CREATE DATABASE wk6pay")

# Displaying existing database list
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

# creating Employee table.
my_cursor.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), name VARCHAR(255), department_id INT)")
# creating Department table
my_cursor.execute("CREATE TABLE Department (id INT AUTO_INCREMENT PRIMARY KEY, departname VARCHAR(255))")

# Displaying Databases
for x in my_cursor:
    print(x)

# close the connection
mydb.close()