from flask import Flask,request,render_template,redirect,jsonify
from controller import Login

app=Flask(__name__)
email_user=Login()

@app.route("/user")
def user_show():
    users=email_user.select()
    return render_template("list.html",users=users)

@app.route("/user/create")
def create_form():
    return render_template("create.html")

#insert
@app.route("/user",method=["POST"])
def insert1():
    data=request.form
    email_user.insert(data.get("name"),data.get("age"))
    return redirect("/user")

if __name__ == "__main__":
    app.run(debug=True, port=8000)