import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    username='nodecarlos',
    password='!Camdes052021!',
    database='client_x'
)

c = db.cursor()

c.execute(
    'DROP TABLE IF EXISTS customers'
)
