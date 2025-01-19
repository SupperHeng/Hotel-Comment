from flask_pymongo import PyMongo

mongo = PyMongo()

def get_hotel_collection():
    return mongo.db.hotels

def get_user_collection():
    return mongo.db.users

def get_review_collection():
    return mongo.db.reviews