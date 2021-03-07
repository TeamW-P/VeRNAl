from flask import Flask, jsonify 
from routes import route

app = Flask(__name__)
app.register_blueprint(route.routes)

@app.route('/', methods=['GET'])
def entry():
    return jsonify(about="Vernal")

if __name__ == '__main__':
    app.run(host="localhost", port=5003, debug=True)
