from pymongo import MongoClient

client = MongoClient(host="192.168.80.147")

mongo_database = client.mydatabase