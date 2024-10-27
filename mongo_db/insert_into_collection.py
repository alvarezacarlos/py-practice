import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = mongo_instance["my_db"] 

my_collection = my_db('customers')

my_dictionary = {'name': 'Carlos', 'age': 25}

#insert a record in the "customers" collection
#The insert_one() method returns an InsertOneResult() object, which has a prperty, inserted_id, that holds the id of the inserted document.
res_obj_created = my_collection.insert_one(my_dictionary)

print(res_obj_created.inserted_id)

# If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document. In the example above no _id field was specified, so MongoDB assigned a unique _id for the record (document).

