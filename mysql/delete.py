import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='nodecarlos',
    password='!Camdes052021!',
    database='client_x'
)

c = db.cursor()

c.execute(
    """
      DELETE FROM customers WHERE id = {}
    """.format(16)
)
db.commit()