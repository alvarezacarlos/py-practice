import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = mongo_instance["my_db"]

my_collection = my_db['customers']

dictionaries_list = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

# To insert multiple documents into a collection in MongoDB, we use the insert_many() method. The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert:

res = my_collection.insert_many(dictionaries_list)

# The insert_many() method returns a InsertManyResult object, which has a property, inserted_ids, that holds the ids of the inserted documents.
#print list of the _id values of the inserted documents:
print(res.inserted_ids)
