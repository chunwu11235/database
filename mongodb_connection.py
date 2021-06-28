import pymongo

client = pymongo.MongoClient('127.0.0.1', 57918)

print(client.list_database_names())
db = client['test']
print(db.list_collection_names())
db.test.find_one()

doc2 = {
    'title': 'inserted from python'
}

db.test.insert_one(doc2)
cursor = db.test.find()
for doc in cursor:
    print(doc)