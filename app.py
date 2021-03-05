from flask import Flash, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(about="Hello from Vernal, WP!")

if __name__ == '__main__':
    app.run(host="localhost", port=5003, debug=True)