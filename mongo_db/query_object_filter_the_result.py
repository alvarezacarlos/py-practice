# When finding documents in a collection, you can filter the result by using a query object. The first argument of the find() method is a query object, and is used to limit the search.

# Find document(s) with the address "Park Lane 38":
import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = mongo_instance["my_db"]

my_collection = my_db['customers']

res = my_collection.fin({ 'age': 40 }) # Find document(s) with the user's age = 40:

for item in res:
    print(item)

