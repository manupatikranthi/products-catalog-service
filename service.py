from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

json_file = open("products.json")
products = json.load(json_file)

@app.route('/')
def get_products():
    return str(products)

if __name__ == "__main__":
    app.run()