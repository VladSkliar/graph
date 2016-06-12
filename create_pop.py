from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collection = db.cities
pop_collection = db.popularity


def summ_pop(data):
    summ = 0
    for obj in data:
        summ += obj['pop']
    return summ


def create_true_pop():
    names = collection.distinct('city')
    states = collection.distinct('state')
    pop = {}
    i = 1
    for state in states:
        for name in names:
            cities = collection.find({'city': name, 'state': state})
            if cities.count() > 0:
                pip = summ_pop(cities)
                pop['city'] = name
                pop['pop'] = pip
                pop['state'] = state
                pop['_id'] = i
                pop_collection.insert_one(pop)
                i += 1
                print i
    print '!!!!!!!!'
