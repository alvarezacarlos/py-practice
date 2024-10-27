import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="nodecarlos",
    password="!Camdes052021!",
    database="client_x"
)
c = db.cursor()

# You can retrieve the table columns: https://pythontic.com/database/mysql/describe
c.execute(
    'DESCRIBE client_x.customers'
)

res_list = c.fetchall()
# print(res_list)
for column in res_list:
    print(column)