#This file will move all route related codes from app.py to movies.py
#Flask-Restful uses Class-based syntax, so if you want to define a resource (API),
#we can just define a class which extends flask-restful's Resource
from flask import Response, request
from database.models import Movie, User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, UpdatingMovieError, DeletingMovieError, MovieNotExistsError

#We will create two different classes: MoviesApi and MovieApi
#MoviesApi will be used to represent the whole document
#MovieApi will be used to manage each individual document
#The reason why these are separated is for organized and clean code.
class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)
    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            movie = Movie(**body, added_by=user)
            movie.save()
            user.update(push__movies=movie)
            user.save()
            id = movie.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise MovieAlreadyExistsError
        except Exception as e:
            raise InternalServerError
#As you can see, we have wrapped the post(self) method, alongside other methods,
#with try...except blocks. What we have done is performed EXCEPTION CHAINING,
#so that when we get any exception, we will use our predefined exceptions
#from errors.py and flask-restful will generate a response based on the values
#we defined in errors dictionary

class MovieApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            movie = Movie.objects().get(id=id, added_by=user_id)
            body = request.get_json()
            Movie.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingMovieError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            movie = Movie.objects().get(id=id, added_by=user_id)
            movie.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingMovieError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            movies = Movie.objects().get(id=id).to_json()
            return Response(movie, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception:
            raise InternalServerError
