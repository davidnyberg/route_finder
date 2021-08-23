from flask import Flask, send_from_directory, request, jsonify
app = Flask(__name__)


# Show svelte app through flask
# Source: https://cabreraalex.medium.com/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9
@app.route("/")
def index():
    return send_from_directory('public', 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory('public', path)

@app.route("/get_trails", methods=['GET', 'POST'])
def get_trails():
    """
    Access open street map overpass API to find trails
    """
    if request.method == 'POST':
        coordinates = request.args.get('coordinates')
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200
    else: #GET
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
    app.run(debug=True)