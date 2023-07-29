from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os 
import logging
from dotenv import load_dotenv


load_dotenv()
uri = os.getenv('DATABASE_URI')
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.StockNews

def ping_db():
    try:
        client.admin.command('ping')
        logging.debug("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        logging.debug(e)
        
def create_collection(symbol):
    try:
        collect = db[symbol]
        logging.info(collect.name)
        print(collect.name) 
        collect.create_index('news_id', unique = True)
    except Exception as e:
        logging.debug(e)
