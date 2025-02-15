from flask import Flask,redirect,render_template,request,jsonify
from user import Student_form
import os
app=Flask(__name__)
acc=Student_form()
UPLOAD_FOLDER = "uploads/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/form", methods=["POST"])
def index1():
    name = request.form.get("name")
    image = request.files.get("image") 
    value1 = request.form.get("value1")
    if image:
        image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_filename)
        image_path = image_filename
    acc.insertdel(name, image_path, value1)


    qul = request.form.get("qul")
    myp = request.form.get("myp")
    uname = request.form.get("uname")
    id_fk=request.get("id_fk")
    acc.insertdelqul(qul, myp, uname,id_fk)
    return jsonify(request.form)


@app.route("/table")
def index2():
    users=acc.display()
    return render_template("table.html",users=users)


@app.route("/table1")
def index3():
    users=acc.displayqul()
    return render_template("table1.html",users=users)




if __name__=="__main__":
    app.run(port=7845)