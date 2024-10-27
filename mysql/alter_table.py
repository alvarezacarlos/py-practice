import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="nodecarlos",
    password="!Camdes052021!",
    database="client_x"
)

c = db.cursor()

c.execute(
    """
        ALTER TABLE customers ADD COLUMN age INT NOT NULL
    """
)
