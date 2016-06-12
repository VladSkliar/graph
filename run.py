from flask import Flask
from flask import render_template
from pymongo import MongoClient
# import flask
import json

app = Flask(__name__, static_url_path='/static')
client = MongoClient('localhost', 27017)
db = client.test
collection = db.cities
pop_collection = db.popularity


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/zipcodes')
def zipcodes():
    return render_template('zipcode.html')


@app.route('/popularity')
def popularity():
    return render_template('pop.html')


@app.route('/mongo_data_zipcode')
def mongo_data_zipcode():
    responce = []
    cities = collection.find().sort('pop', -1).limit(20)
    for city in cities:
        responce.append(city)
    return json.dumps(responce)


@app.route('/mongo_data_city')
def mongo_data_city():
    responce = []
    cities = pop_collection.find().sort('pop', -1).limit(20)
    for city in cities:
        responce.append(city)
    return json.dumps(responce)


if __name__ == '__main__':
    app.run(use_reloader=True,
            host='0.0.0.0',
            port=5002)
