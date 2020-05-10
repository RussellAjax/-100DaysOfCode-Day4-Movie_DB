from .db import db

#Create a document for our database. Ensures that users
#cannot add other fields other the three fields defined
#in this field. 

#We can see that the Movie doucment has three fields:
#   1.name  : is a field of type String, there are also two
#           constraints in this field:
#           `required`  : which means the user cannot create a movie
#                       without the title.
#           `unique`    : which means that the movie name cannot be repeated

#   2. casts: is a field of type List, which contains values of type String
#   3. genres: same value as casts

class Movie(db.Document):
    name = db.StringField(required = True, unique = True)
    casts = db.ListField(db.StringField(), required = True)
    genres = db.ListField(db.StringField(), required = True)

