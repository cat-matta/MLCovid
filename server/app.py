import pymongo
import dns
import os
from dotenv import load_dotenv

load_dotenv()
Mongo_URI = os.getenv('dburi')
client = pymongo.MongoClient(Mongo_URI)
db = client.get_database("MLCovid")

new_item= {
      'Name': 'Youtube',
      'Type': 'Comment'
}
db['Scrapped_Data'].insert_one(new_item)
want=db['Scrapped_Data'].find_one({'Name':"Youtube"}) # to locate the entry
print(want['Type'])