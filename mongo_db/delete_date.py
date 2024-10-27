import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = mongo_instance["my_db"]

my_collection = my_db['customers']

# To delete one document, we use the delete_one() method. The first parameter of the delete_one() method is a query object defining which document to delete.
# If the query finds more than one document, only the first occurrence is deleted.

#Delete many documents where usre is equal to 30
my_collection.delete_one({ 'age': 30 })



# Delete All Documents in a Collection. Delete all documents in the "customers" collection:
res = mycol.delete_many({})
print(res.delete_count, " docyuments deleted")