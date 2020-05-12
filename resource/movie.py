#This file will move all route related codes from app.py to movies.py
from flask import Blueprint, Response, request
from database.models import Movie

#Creates a new Blueprint
movies = Blueprint('movies', __name__)
#__name__ is a special Python variable that contains the name of this module (movie.py)


#GET request for the whole document
@movies.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

#GET request for only ONE part of the document
@movies.route('/movies/<id>', methods=['GET'])
def get_movie():
    movie = Movie.objects().get(id=id).to_json()
    return Response(movie, mimetype="application/json", status 200)

#POST request
@movies.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return{'id': str(id)}, 200

#PUT reqeust
@movies.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects().get(id=id).update(**body)
    return '', 200

#DELETE request
@movies.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects().get(id=id).delete()
    return '', 200


