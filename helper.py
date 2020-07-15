import pymongo
import os.path
from nltk import framenet as fn


def getText:
    if (mongoClient != None)
        MongoClient mongoClient = new MongoClient()

    dbList = mongoClient.list_database_names()
    if processed_data not in dbList):
        exists = os.path.isfile('\downloads\data_filter.json')
        if not exists:
            print("json file doesn't exist")
            dbList = mongoClient.list_database_names()
            break
        load("\downloads\data_filter.json")

    db.processed_data.find({"text":{}})


def getStory:
    if (mongoClient != None)
        MongoClient mongoClient = new MongoClient()
    if processed_data not in dbList):
        exists = os.path.isfile('\downloads\data_filter.json')
        if not exists:
            print("json file doesn't exist")
            break
        load("\downloads\data_filter.json")
    db.processed_data.find({"story":{}})

###
#How to load Json into a MongoDB database:
# Download data (json file from GitHub) 
# Use <mongoimport> to insert docs
# Put json file in downloads

#In terminal:
#mongoimport --db <database_name> --collection <collection_name> --file ~\downloads\inventory.crud.json

#mongoimport --db framenet --collection processed_data    --drop --file ~\downloads\inventory.crud.json