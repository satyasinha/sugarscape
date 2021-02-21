from flask import Flask, send_from_directory, request
import random
from model import sugarscape

app = Flask(__name__)


# Path for main app
@app.route("/")
def base():
  return send_from_directory('view/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
  return send_from_directory('view/public', path)

@app.route("/model", methods = ['GET', 'POST'])
def model():
  world = []
  if request.method == 'POST':
    world = sugarscape.environment(request.json['gridSize'])
    world.initEnvironment(request.json['numTurtles'], request.json['initSugars'])
    return str(request.json['gridSize'])
  else:
    return str(world.width)

if __name__ == "__main__":
    app.run(debug=True)