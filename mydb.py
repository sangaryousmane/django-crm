import mysql.connector as db

# Add host, username and password
dataBase = db.connect(
    host = 'localhost',
    user = 'root',
    password = ""
)

# Prepare a cursor object
cursorObj = dataBase.cursor()

# execute the database create command
cursorObj.execute("CREATE DATABASE elderco")
print("DONE ALL")