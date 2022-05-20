from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def index() -> str:
    with open('contents.html') as contents:
        return contents.read()


@app.route('/add', methods=['POST'])
def add() -> Response:
    data = request.get_json()
    return jsonify(
        total=sum(data.values()),
    )


@app.route('/mult', methods=['POST'])
def mult() -> Response:
    data = request.get_json()
    return jsonify(
        product=data['a'] * data['b'] * data['c'],
    )


@app.route('/min_and_max', methods=['POST'])
def min_and_max() -> Response:
    data = request.get_json()
    return jsonify(
        max=max(data.values()),
        min=min(data.values())
    )
