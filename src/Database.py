import pymongo
from datetime import datetime
from ConfigFactory import ConfigFactory


class Database:
    def __init__(self, conf=ConfigFactory.create_app_config()):
        self.__host = conf.Database.Host
        self.__client = pymongo.MongoClient(self.__host)
        self.__db = self.__client[conf.Database.DbName]
        self.users_collection = self.__db[conf.Database.UsersCollection]
        self.feedbacks_collection = self.__db[conf.Database.FeedbacksCollection]

    def current_utc_time_str(self):
        return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    def save(self, first_name, last_name, phone_num, email, password, company_name):
        self.users_collection.update(
            {"email": email},
            {"$set": {
                "last_login_time": self.current_utc_time_str()
            }, "$setOnInsert": {
                'first_name': first_name,
                'last_name': last_name,
                'phone_num': phone_num,
                'password': password,
                'company_name': company_name
            }}, upsert=True)
