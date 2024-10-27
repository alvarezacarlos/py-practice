import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = mongo_instance["my_db"]

my_collection = my_db['customers']

res = my_collection.find().limit(5)


for itme in res:
    print(item)