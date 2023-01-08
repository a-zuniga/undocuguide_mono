from dotenv import load_dotenv
from pymongo import MongoClient
from models import Scholarship
import os

load_dotenv()
DB_URI = os.environ.get('MONGO_URI')
client = MongoClient(DB_URI)
db = client["UndocuGuide"]
scholarship_collection = db["Scholarships"]

def create_scholarship_in_db(scholarship: Scholarship):
    scholarship_collection.insert_one(scholarship.__dict__)

def read_scholarship_from_db(scholarship_id):
    return scholarship_collection.find_one({'_id': scholarship_id})

def update_scholarship_in_db(scholarship_id, scholarship):
    scholarship_collection.update_one({'_id': scholarship_id}, {'$set': scholarship.__dict__})

def delete_scholarship_from_db(scholarship_id):
    scholarship_collection.delete_one({'_id': scholarship_id})