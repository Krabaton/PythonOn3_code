from flask import Flask
import os
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://db:27017/book")
db = client.book


@app.route('/')
def hello():
    result = {}
    data = db.cats.find({})
    for el in data:
        result.update({f"{el.get('_id')}": el.get("name")})
    return result


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=5000)
