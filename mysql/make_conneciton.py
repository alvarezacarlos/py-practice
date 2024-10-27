#Python needs a MySQL driver to access the MySQL database.
#Install the driver: mysql-connector-python
# pip3 install mysql-connector-python

import mysql.connector # If the above code was executed with no errors, "MySQL Connector" is installed and ready to be used.

#Make the connection the server
db = mysql.connector.connect(
    host="localhost",
    user="nodecarlos",
    password="!Camdes052021!"
)

print(db) #now we can start running scripts