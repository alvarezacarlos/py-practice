import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = mongo_instance["my_db"]

my_collection = my_db['customers']

# In MongoDB we use the find and findOne methods to find data in a collection. Just like the SELECT statement is used to find data in a table in a MySQL database.

# find_one() : The find_one() method returns the first occurrence in the selection.
res = my_collection.find_one()

print(res)