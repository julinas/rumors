import pymongo
from pymongo import MongoClient
from nltk import framenet as fn


class Helper:
    __db = None
    def __init__(self):
        #Initialize your database connection here.
        if Helper.__db == None:
            Helper.__db = connect('localhost:27017/framenet')

    def getDatabase():
      # Static access method. 
      if Helper.__db == None:
         Helper()
      return Helper.__db

    def getTextFromData():
        if (mongoClient == None)
            mongoClient = MongoClient()

        dbList = mongoClient.list_database_names()
        if framenet not in dbList):
            db = Helper.getDatabase()

        db.p_data.find({}, {"text":1})


    def getStoryFromData():
        if (mongoClient == None)
            mongoClient = MongoClient()

        if framenet not in dbList):
            db = Helper.getDatabase()

        db.p_data.find({}, {"story":1})

#we can't find a way to access specific docs so we decided to create a method 
#that would operate with a collection of documents that have an "index" field as well. 
    def getEntry(index):
        processed_data = db.p_data
        #document = db.processed_data.find("index": index)
        textList = getTextFromData()
        text = textList[index]
        #text = document["text"]
        #text = document["story"]
        storyList = getStoryFromData()
        story = storyList[index]
        entry = (text, story)
        return entry



###
#How to load Json into a MongoDB database:
# Download data (json file from GitHub) 
# Use <mongoimport> to insert docs
# Put json file in downloads

#In terminal:
#mongoimport --db <database_name> --collection <collection_name> --file ~\downloads\inventory.crud.json

#mongoimport --db framenet --collection processed_data    --drop --file ~\downloads\inventory.crud.json