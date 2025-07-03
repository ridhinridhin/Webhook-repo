from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Ridhinridhin:Laya0903@cluster0.qeufq24.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client['webhookDB']
collection = db['events']

def insert_event(data):
    collection.insert_one(data)

def get_all_events():
    return list(collection.find({}, {'_id': 0}))
