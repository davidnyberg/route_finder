from flask import Flask, send_from_directory

app = Flask(__name__)


# Show svelte app through flask
# Source: https://cabreraalex.medium.com/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9
@app.route("/")
def index():
    return send_from_directory('public', 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory('public', path)

@app.route("/get_trails")
def get_trails(coordinates):
    """
    Access open street map overpass API to find trails
    """
    print(f"in osm api called with: {coordinates}", flush = True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
    app.run(debug=True)