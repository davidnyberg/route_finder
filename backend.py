from flask import Flask, send_from_directory, request, jsonify
import logging
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Show svelte app through flask
# Source: https://cabreraalex.medium.com/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9
@app.route("/")
def index():
    return send_from_directory('public', 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory('public', path)

@app.route("/get_trails", methods=['POST'])
def get_trails():
    """
    Access open street map overpass API to find trails
    """
    coordinates = request.json('coordinates')
    app.logger.info(coordinates)
    print('hello', flush=True)
    return 'Sucesss', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)