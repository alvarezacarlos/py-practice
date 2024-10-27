import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="nodecarlos",
    password="!Camdes052021!"
)
c = db.cursor()

c.execute(
    'CREATE DATABASE client_x'
)
