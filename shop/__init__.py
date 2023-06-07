from flask import Flask, render_template,request
import pymongo

app = Flask(__name__)

import os
picfolder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = picfolder

# s = '\''

db_client = pymongo.MongoClient("mongodb://localhost:27017")
# db = db_client["students"]
# mark_table = db["mark"]

db = db_client.test_db
test_collection = db.test_collection
test_collection2 = db.test_collection2
test_collection_3 = db.test_collection_3
test_collection_4 = db.test_collection_4
from shop import routes
