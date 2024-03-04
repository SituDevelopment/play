import config
import pymongo.mongo_client as pm

client = pm.MongoClient(config.MONGO_HOSTNAME)
