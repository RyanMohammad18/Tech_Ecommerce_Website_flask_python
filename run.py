from flask import Flask,render_template
from pymongo import MongoClient

from shop import app

# app = Flask(__name__)

# client = MongoClient('localhost', 27017)


if __name__ == "__main__":
    app.run(debug=True,port=2000)