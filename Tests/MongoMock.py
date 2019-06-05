from pymongo import MongoClient

mongo_url = 'mongodb://localhost:27017'
client = MongoClient(mongo_url)
db = client.db
