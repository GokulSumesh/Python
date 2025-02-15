import mysql.connector

class Register_form:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="register_form"
        )
        self.cursor=self.conn.cursor(dictionary=True)

    def insert(self,name,age,dob,email,password):
        query="insert into user_details(name,age,dob,email,password)values(%s,%s,%s,%s,%s)"
        self.cursor.execute(query,(name,age,dob,email,password))
        self.conn.commit()

    def display(self):
        self.cursor.execute("SELECT * from user_details")
        users = self.cursor.fetchall()
        return users

    def display_id(self,id):
        query="select * from user_details where id=%s"
        self.cursor.execute(query,(id,))
        users=self.cursor.fetchone()
        return users

    
    def delete(self,id):
        query="delete from user_details where id =%s"
        self.cursor.execute(query,(id,))
        self.conn.commit()

    def update(self,name,age,dob,email,password,id):
        query="update user_details set name=%s,age=%s,dob=%s,email=%s,password=%s where id=%s"
        self.cursor.execute(query,(name,age,dob,email,password,id))
        self.conn.commit()



