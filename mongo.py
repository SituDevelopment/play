import pymongo.mongo_client as pm

import config

client = pm.MongoClient(config.MONGO_HOSTNAME)
