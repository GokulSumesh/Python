import mysql.connector

class Student_form:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="student_form"
        )
        self.cursor=self.conn.cursor(dictionary=True)

    def insertdel(self,name,image,value1):
        query="insert into student_details(name,image,value1)values(%s,%s,%s)"
        self.cursor.execute(query,(name,image,value1))
        self.conn.commit()

    def display(self):
        self.cursor.execute("select * from student_details")
        users = self.cursor.fetchall()
        return users

    def display_id(self,id):
        query="select * from student_details where id=%s"
        self.cursor.execute(query,(id,))
        users=self.cursor.fetchone()
        return users


    def insertdelqul(self, qul, myp, uname,id_fk):
        query = "INSERT INTO student_qul ( qul, myp, uname,id_fk) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (qul, myp, uname,id_fk))
        self.conn.commit()

    def displayqul(self):
        self.cursor.execute("select * from student_qul")
        users = self.cursor.fetchall()
        return users

    # def display_idqul(self,id):
    #     query="select * from student_qul where id=%s"
    #     self.cursor.execute(query,(id,))
    #     users=self.cursor.fetchone()
    #     return users









    








