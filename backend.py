from flask import Flask, send_from_directory, request, jsonify
from flask.wrappers import Response
import overpy
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

@app.route("/get_trails", methods=['GET'])
def get_trails():
    """
    Access open street map overpass API to find trails
    """
    coordinates = request.args.get('coordinates')
    trails = OSM_api(coordinates=coordinates)
    return Response('Sucesss', 200)

def OSM_api(coordinates=None):
    '''
    https://python-overpy.readthedocs.io/en/latest/
    Calls overpass api
    '''
    api = overpy.Overpass()

    app.logger.info(coordinates)

    # fetch all ways and nodes
    # placeholder call
    result = api.query("node(50.745,7.17,50.75,7.18);out;")

    return Response('Trail info', 200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)