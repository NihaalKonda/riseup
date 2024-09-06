import pymongo
class Database:
    DB = None
    @staticmethod
    def initialize():
        client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        Database.DB = client.mydb
    @staticmethod
    def insert_record(docutest):
        Database.DB.users.insert(docutest)
    @staticmethod
    def show_docs():
        records = [docu for docu in Database.DB.users.find({})]
        return records