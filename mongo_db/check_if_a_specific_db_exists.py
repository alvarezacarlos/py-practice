

import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

db_list = mongo_instance.list_database_names()

if "my_db" in db_list:
  print("The database exists.")