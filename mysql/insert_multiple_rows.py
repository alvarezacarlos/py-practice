import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="nodecarlos",
    password="!Camdes052021!",
    database="client_x"
)

c = db.cursor()

list_of_tuples = [
    ('user_3', 'password_of_u3', 33),
    ('user_4', 'password_of_u4', 45),
    ('user_5', 'password_of_u5', 43),
    ('user_6', 'password_of_u6', 44),
    ('user_7', 'password_of_u7', 62),
    ('user_8', 'password_of_u8', 28),
    ('user_9', 'password_of_u9', 30),
    ('user_10', 'password_of_u10', 66),
    ('user_11', 'password_of_u11', 52),
    ('user_12', 'password_of_u12', 27),
    ('user_13', 'password_of_u13', 41),
    ('user_14', 'password_of_u14', 72),
    ('user_15', 'password_of_u15', 40)
]

c.executemany(
    """
        INSERT INTO client_x.customers
        (username, password, age)
        values
        (%s, %s, %s)
    """, list_of_tuples #('user_2', 'user_2_password', 30)
)
db.commit()


#You can get the id of the row you just inserted by asking the cursor object.  If you insert more than one row, the id of the last inserted row is return
print("1 record inserted, ID:", c.lastrowid)