#Import Flask and jsonify class from
#the "flask" package.
from flask import Flask, jsonify
app = Flask(__name__)


#Creating a Movies list that will be converted
#into a JSON value because of jsonify
movies = [
        {
            "name": "Fight Club",
            "casts": ["Brad Pitt", "Edward Norton", "Helena Bonham Carter", "Meat Loaf"],
            "genres": ["Thriller"]
            },
        {
            "name": "The Godfather",
            "casts": ["Marlon Brando", "Al Pacino", "James caan", "Diane Keaton"],
            "genres": ["Crime", "Drama"]
            }
        ]

#Define root endpoint with @app.route('/movies')
#This means that the API will be accessible from
#http://localhost:5000/movies/?false=true
@app.route('/movies')

#hello() returns the JSON value
#of the movies list created above
def hello():
    return jsonify(movies)

#Flask server is started with app.run()
app.run()
