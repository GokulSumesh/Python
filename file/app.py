from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def index1():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f'File successfully uploaded to {filepath}'

if __name__ == "__main__":
    app.run(debug=True, port=4125)