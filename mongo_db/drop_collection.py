# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.

# Delete the "customers" collection:

import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = mongo_instance["my_db"]

my_collection = my_db['customers']


#The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.
res = my_collection.drop() # drop the customers collection.
print(res)