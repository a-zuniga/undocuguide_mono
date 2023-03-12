from dotenv import load_dotenv
from pymongo import MongoClient
from models import Scholarship
import os
from bson.objectid import ObjectId

load_dotenv()
DB_URI = os.environ.get('MONGO_URI')
client = MongoClient(DB_URI)
db = client["UndocuGuide"]
scholarship_collection = db["Scholarships"]


def create_scholarship_in_db(scholarship: Scholarship):
    return scholarship_collection.insert_one(scholarship.__dict__)

def read_scholarship_from_db(scholarship_id):
    return scholarship_collection.find_one({'_id': ObjectId(scholarship_id)})

def update_scholarship_in_db(scholarship_id, fields_to_update):
    update_query = scholarship_collection.find_one_and_update(
    {'_id': ObjectId(scholarship_id)}, 
    {'$set': fields_to_update})

    return update_query

def delete_scholarship_from_db(scholarship_id):
    deleted_scholarship = scholarship_collection.find_one_and_delete({'_id': ObjectId(scholarship_id)})
    return deleted_scholarship