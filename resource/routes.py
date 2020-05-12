from .movie import MovieApi, MoviesApi

#Using the routes.py file, you can determine the path of the endpoint
#Here, we programmed the computer so that the path it follows is /api/movies,
#instead of just /movies
def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies') #The whole movie document
    api.add_resource(MovieApi, '/api/movies/<id>') #By specific id

