from flask import Flask,render_template,jsonify
app=Flask(__name__)

@app.route("/")
def index():
    return jsonify("This is Index Page")

@app.route("/about")
def index1():
    return render_template("html1/about.html")

@app.route("/contact")
def index2():
    return render_template("html1/contact.html")

@app.route("/home")
def index3():
    return render_template("html1/home.html")


@app.route("/gallery")
def index4():
    return render_template("html2/gallery.html")


@app.route("/profile")
def index5():
    return render_template("html2/profile.html")


@app.route("/resources")
def index6():
    return render_template("html2/resources.html")

@app.route("/form")
def index7():
    return render_template("html3/form.html")

@app.route("/photo")
def index8():
    return render_template("html3/photo.html")

@app.route("/table")
def index9():
    return render_template("html3/table.html")


if __name__=="__main__":
    app.run(port=6500)


