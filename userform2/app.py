from flask import Flask,render_template,jsonify,request,redirect
from user import User
app=Flask(__name__)
acc=User()

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/form",methods=["POST"])
def index1():
    username=request.form.get("name")
    phone=request.form.get("phone")
    email=request.form.get("email")
    password=request.form.get("password")
    acc.insert(username,phone,email,password)
    return jsonify(request.form)

@app.route("/table")
def index2():
    users=  acc.display()
    return render_template("table.html",users=users)

@app.route("/delete/<int:id>")
def index3(id):
    acc.delete(id)
    return redirect("/table")

@app.route("/update/<int:id>")
def index4(id):
    users = acc.display_id(id)
    return render_template("edit.html", users=users)

@app.route("/update/<int:id>", methods=["POST"])
def index5(id):
    data=request.form
    acc.update(data.get("name"),data.get("phone"),data.get("email"),data.get("password"),id)
    return redirect("/table")


if __name__=="__main__":
    app.run(port=6321)






