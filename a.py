from flask import Flask, jsonify

app = Flask(__name__)

# Define a route to handle requests
@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

if __name__ == "__main__":
    app.run(port=7000)