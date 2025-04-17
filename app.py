from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='public', static_url_path='/public')
CORS(app)

data_store = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/data', methods=['POST'])
def post_data():
    if not request.is_json:
        return jsonify({"error": "JSON required"}), 400
    item = request.get_json()
    data_store.append(item)
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(debug=True)
