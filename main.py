from flask import Flask # Import API package.

api = Flask(__name__) # Declare the API

@api.route("/")
def say_hello():
    return "Hello, the API is up and running."

api.run() # Run the API

# <urlink>/hello --> Hello there!