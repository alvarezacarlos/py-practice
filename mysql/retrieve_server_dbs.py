import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="nodecarlos",
    password="!Camdes052021!",
    database="client_x"
)

c = db.cursor()


#Chech if the db exists
c.execute("SHOW DATABASES")

for database in c:  
    print(database)