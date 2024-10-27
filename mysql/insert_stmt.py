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
        INSERT INTO client_x.customers
        (username, password, age)
        values
        (%s, %s, %s)
    """, ('user_2', 'user_2_password', 30)
)
db.commit()

#You can get the id of the row you just inserted by asking the cursor object.  If you insert more than one row, the id of the last inserted row is return
print("1 record inserted, ID:", c.lastrowid)