from flask import Flask,render_template,jsonify,request
from user import User
app=Flask(__name__)
acc=User()


@app.route("/")
def index():
    return render_template("form.html")

@app.route("/dba",methods=["POST"])
def index1():
    username=request.form.get("username")
    phone=request.form.get("phone")
    email=request.form.get("email")
    password=request.form.get("password")
    acc.insert(username,phone,email,password)
    return jsonify(request.form)

@app.route("/table")
def index2():
    users = acc.get_users() 
    return render_template("table.html", users=users)




   

if __name__=="__main__":
    app.run(port=5478)


