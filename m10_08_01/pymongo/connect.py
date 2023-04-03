from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://userweb10:password@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority",
                     server_api=ServerApi('1'))
db = client.web10

if __name__ == '__main__':
    cats = db.cats.find()
    print(cats)
    for cat in cats:
        print(cat['_id'], cat['name'], cat['age'])
