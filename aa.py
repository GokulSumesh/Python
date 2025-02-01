from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "This is the root URL"})

@app.route("/home")
def index1():
    # Ensure home.html exists in the templates folder
    return render_template("home.html")

@app.route("/dashboard")
def index2():
    return jsonify({"message": "This is the dashboard URL"})

if __name__ == "__main__":
    app.run(port=7000)
