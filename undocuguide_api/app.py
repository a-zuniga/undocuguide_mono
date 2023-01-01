from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient
import os

load_dotenv()
app = Flask(__name__)
DB_URI = os.environ.get('MONGO_URI')

from controllers import scholarships
app.register_blueprint(scholarships)

client = MongoClient(DB_URI)
db = client["UndocuGuide"]

if __name__ == '__main__':
    app.run()
