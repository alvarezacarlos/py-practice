import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="nodecarlos",
    password="!Camdes052021!",
    database="client_x"
)

c = db.cursor()

#you can check if a table exists by listing all the tables in your database with the "SHOW TABLES" statement.
c.execute("SHOW TABLES")

for table in c:
    print(table) # it returns a tuple: ('customers',)
