# A collection in MongoDB is the same as a table in SQL databases.

# To create a collection in MongoDB, use database object and specify the name of the collection you want to create. MongoDB will create the collection if it does not exist.


import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = mongo_instance["my_db"]

my_collection = my_db["customers"]