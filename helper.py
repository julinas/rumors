from pymongo import MongoClient



class MongoHelper:
    __db = None
    @classmethod
    def __init__(cls):
        #Initialize your database connection here.
        client = MongoClient('127.0.0.1', 27017)
        if MongoHelper.__db == None:
            MongoHelper.__db = client["framenet"]

    @classmethod       
    def getDB(cls):
        return MongoHelper.__db
    @classmethod
    def getTextFromData(cls):
        # if (mongoClient == None)
        #     mongoClient = MongoClient()
        # if framenet not in dbList):
        #     db = Helper.getDatabase()
        texts = []
        docs = MongoHelper.getDB().p_data.find({})
        for i in docs:
            txt = i["text"]
            texts.append(txt)
        return texts

    @classmethod
    def getStoryFromData(cls):
        # if (mongoClient == None)
        #     mongoClient = MongoClient()

        # if framenet not in dbList):
        #     db = Helper.getDatabase()
        stories = []
        docs = MongoHelper.getDB().p_data.find({})
        for i in docs:
            story = i["story"]
            stories.append(story)
        return stories
    @classmethod
    def getAllEntries(cls):
        entries = []
        docs = MongoHelper.getDB().p_data.find({})
        for i in docs:
            text = i["text"]
            story = i["story"]
            entry = (text,story)
            entries.append(entry)
        return entries

#we can't find a way to access specific docs so we decided to create a method 
#that would operate with a collection of documents that have an "index" field as well. 
    # def getEntry(index):
    #     processed_data = db.p_data
    #     #document = db.processed_data.find("index": index)
    #     textList = getTextFromData()
    #     text = textList[index]
    #     #text = document["text"]
    #     #text = document["story"]
    #     storyList = getStoryFromData()
    #     story = storyList[index]
    #     entry = (text, story)
    #     return entry



###
#How to load Json into a MongoDB database:
# Download data (json file from GitHub) 
# Use <mongoimport> to insert docs
# Put json file in downloads

#In terminal:
#mongoimport --db <database_name> --collection <collection_name> --file ~\downloads\inventory.crud.json

#mongoimport --db framenet --collection processed_data    --drop --file ~\downloads\inventory.crud.json