#Import Flask and jsonify class from
#the "flask" package.
from flask import Flask, jsonify, request
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
#hello() returns the JSON value
#of the movies list created above
@app.route('/movies')
def hello():
    return jsonify(movies)

#As you can see, @app.route() can take one more argument
#in addition to the API endpoint: the methods (POST, PUT, DELETE)

#This endpoint will add a new movie to our movies list
#This endpoint accepts POST request, which will allow
#the user to send a new movie for the list.
@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

#This endpoint will allow for editing the movie
#which already exists in the list based on its
#index as suggested by <int:index>
@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200

#This endpoint will delete hte movie form the given index
#of movie list.
@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return 'None', 200

#Flask server is started with app.run()
app.run()
