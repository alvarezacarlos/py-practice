import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    username='nodecarlos',
    password='!Camdes052021!',
    database='client_x'
)

c = db.cursor()

id = 1

c.execute(
    "UPDATE customers SET age = 50 WHERE id = %s", (id,)
)
db.commit()