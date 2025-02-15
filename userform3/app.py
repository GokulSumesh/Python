from flask import Flask,redirect,render_template,jsonify,request
from user import Register_form
app=Flask(__name__)
acc=Register_form()

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/form",methods=["POST"])
def index1():
    # name=request.form.get("name")
    # age=request.form.get("age")
    # dob=request.form.get("dob")
    # email=request.form.get("email")
    # password=request.form.get("password")
    # acc.insert(name,age,dob,email,password)
    # return jsonify(request.form)
    data=request.form
    acc.insert(data.get("name"),data.get("age"),data.get("dob"),data.get("email"),data.get("password"))
    return jsonify(data)

@app.route("/table")
def index2():
    users=acc.display()
    print(users)
    return render_template("table.html",users=users)

@app.route("/delete/<int:id>")
def index3(id):
    acc.delete(id)
    return redirect("/table")

@app.route("/update/<int:id>")
def index4(id):
    users=acc.display_id(id)
    return render_template("edit.html",users=users)



@app.route("/update/<int:id>",methods=["POST"])
def index5(id):
    data=request.form
    acc.update(data.get("name"),data.get("age"),data.get("dob"),data.get("email"),data.get("password"),id)
    return redirect("/table")
    

    


if __name__=="__main__":
    app.run(port=6547)
