
import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

print(mongo_instance.list_database_names())


