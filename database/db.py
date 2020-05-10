#Imports MongoEngine class from flask_mongoengine library
from flask_mongoengine import MongoEngine

#Creates the db object
db = MongoEngine()

#Defines function initialize_db()
#which we will call app.py to initialize
#the database
def initialize_db(app):
    db.init_app(app)
