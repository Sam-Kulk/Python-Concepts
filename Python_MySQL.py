# Whenever I want to work with any RDBMS, there will be a dedicated package of that which i need to install & make use of
# Ex for MySQL - mysql-connector-python package I need to install
# Then I need to import that in my file
import mysql.connector

# After importing the package I need to connect to db
connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database='world')
print(connection) # prints MySQL connection object

# I need to create cursor object to interact with database
mycursor = connection.cursor()

# Then I can execute the statements, with execute() method
mycursor.execute("show tables") # in execute the statement that I provide needs to be of str datatype
result_set = mycursor.fetchall() # This is used to fetch the result_set in list of tuple format, python can be used on it, otherwise it will return null
print(result_set) # result set will be list of tuples, each tuple is one record in result set with values seperated by comma

# if I want to execute another statement, this is the way
mycursor.execute("show databases")
print(mycursor.fetchall())