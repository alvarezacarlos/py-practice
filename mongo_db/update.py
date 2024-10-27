# You can update a record, or document as it is called in MongoDB, by using the update_one() method. The first parameter of the update_one() method is a query object defining which document to update.



import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = mongo_instance["my_db"]

my_collection = my_db['customers']

# Change the address from "Valley 345" to "Canyon 123":


myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mu_collection.update_one({ 'age':40 }, { '$set' : { 'name': 'Jhon'}})
