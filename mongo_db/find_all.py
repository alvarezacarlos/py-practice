import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = mongo_instance["my_db"]

my_collection = my_db['customers']

# In MongoDB we use the find and findOne methods to find data in a collection. Just like the SELECT statement is used to find data in a table in a MySQL database.

# find() : The find() method returns all occurrences in the selection.
# The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection. No parameters in the find() method gives you the same result as SELECT * in MySQL.
res = my_collection.find()

for item in res:
    print(item)


#Returning only some fields
# The second parameter of the find() method is an object describing which fields to include in the result. This parameter is optional, and if omitted, all fields will be included in the result.

res_1 = mycol.find({},{ "_id": 0, "name": 1, "address": 1 }) # Return only the names and addresses, not the _ids:
for item in res_1:
    print(item)

#You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). If you specify a field with the value 0, all other fields get the value 1, and vice versa:

res_2 = mycol.find({},{ "address": 0 })
for item in res_2:
    print(item)

