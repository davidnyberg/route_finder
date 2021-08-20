from flask import Flask, send_from_directory

app = Flask(__name__)


# Show svelte app through flask
# Source: https://cabreraalex.medium.com/svelte-js-flask-combining-svelte-with-a-simple-backend-server-d1bc46190ab9
@app.route("/")
def index():
    return send_from_directory('svelte-app/public', 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory('svelte-app/public', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)