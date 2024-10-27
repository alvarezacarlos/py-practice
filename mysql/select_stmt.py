import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    username="nodecarlos",
    password="!Camdes052021!",
    database="client_x"
)
c = db.cursor()

c.execute(
    'SELECT * FROM customers'
)

res = c.fetchall()  # We use the fetchall() method, which fetches all rows from the last executed statement.
#fetchone : If you are only interested in one row, you can use the fetchone() method. The fetchone() method will return the first row of the result:

# you can also use the next stmts in you sql queries: WHERE, ORDER BY, Placeholders: {}, %s.

for row in res:
    print(row)
