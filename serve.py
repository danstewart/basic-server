from flask import Flask, json
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/check")
def check():
    return 'Up'

@app.route("/<file>")
def index(file):
    file_path = os.path.join(app.root_path, 'data', file)

    if not os.path.isfile(file_path):
        return 'File not found'

    data = json.load(open(file_path))
    return data

if __name__ == "__main__":
    app.run(debug=True)
