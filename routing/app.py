from flask import Flask,render_template
app=Flask(__name__)

@app.route("/<id>")
def index(id):
#     # return render_template ("root.html")
#     # return jsonify ("Hai")
    return "hello %s" %id
    

@app.route("/home")
def index1():
    return render_template("home.html")

@app.route("/dashboard")
def index2():
    return render_template("dashboard.html")

@app.route("/form1")
def index3():
    return render_template("form1.html")


if __name__=="__main__":
    app.run(port=6500)


