import os
from dotenv import load_dotenv
# from motor.motor_asyncio import AsyncIOMotorClient
# from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pymongo



load_dotenv()
# Función para obtener un cliente de MongoDB asíncrono
def get_mongo_client():
    uri = f"mongodb+srv://Aquirre12:Conext123@mongodbtest.w3d21.mongodb.net/?retryWrites=true&w=majority&appName=MongoDBtest"
    
    try:
        # uri = "mongodb://Aquirre12:Conext123@mongodbtest.w3d21.mongodb.net/"
        client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
        return client
    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
#{os.environ["DB_USER"]}

