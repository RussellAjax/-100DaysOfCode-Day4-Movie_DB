from flask import Flask
app = Flask(__name__)
#Imported the Flask class from flask package

#Define root endpoint with @app.route('/')
#Remember what an endpoint is: the "main"
#Address that we are going to visit
@app.route('/')
#@app.route() is called a decorator
#which basically takes function hello()
#extends its behavior so that it is invoked
#when / endpoints is requested


#hello() returns 
#{'hello': 'world'}

def hello():
    return{'hello': 'world'}

#Flask server is started with app.run()
app.run()
