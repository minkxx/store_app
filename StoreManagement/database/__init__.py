import certifi
from pymongo.mongo_client import MongoClient
from datetime import datetime

from StoreManagement.logger import log

class Database:
    def __init__(self):
        try:
            log.info("configuring database...")
            self.mongoClient = MongoClient("mongodb+srv://minkxx:z8ve7sfrdk@storeapp.rdmtenp.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
            log.info("database configured")
        except Exception as e:
            log.error(e)
        self.db = self.mongoClient["app_database"]
        self.test_collection = self.db["test_collection"]
        
    def insertData(self, name, item_name, quantity):
        self.now_date = datetime.now().date()
        sample_data = {str(name):{"item_name": str(item_name),"quantity": int(quantity),"date_added": str(self.now_date)}}
        self.test_collection.insert_one(sample_data)
        log.info(f"pushed name {name}")

    def getData(self, name):
        query = {name:{"$exists":True}}
        item = self.test_collection.find_one(query)
        return item
        log.info(f"fetched data of user : {name}")

    def updateData(self, name, update_field, new_data):
        query = {name:{"$exists":True}}
        updateQuery = {"$set":{f"{name}.{update_field}": new_data}}
        self.test_collection.update_one(query, updateQuery)
        log.info(f"updated data from {update_filed} to {new_data} of user : {name}")

    def deleteData(self, name):
        query = {str(name):{"$exists":True}}
        self.test_collection.delete_one(query)
        log.info(f"deleted {name}")

    def insertCred(self, username, password):
        sample_data = {"cred":{"username": str(username),"password": str(password)}}
        self.test_collection.insert_one(sample_data)
        log.info(f"pushed name cred {username} and {password}")