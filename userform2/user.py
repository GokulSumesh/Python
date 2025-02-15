import mysql.connector

class User:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="login_user"
        )
        
        self.cursor=self.conn.cursor(dictionary=True)

    def insert(self,name,phone,email,password):
        
        query="insert into users_detail(name,phone,email,password)values(%s,%s,%s,%s)"
        self.cursor.execute(query,(name,phone,email,password))
        self.conn.commit()

    def display(self):
        self.cursor.execute("SELECT * from users_detail")
        users = self.cursor.fetchall()
        print(users)
        return users

    def display_id(self, id):
        sql = "select * from users_detail where id=%s"
        self.cursor.execute(sql, (id,))
        users =self.cursor.fetchone()
        print(users)
        return users



    def delete(self,id):
        sql="delete from users_detail where id=%s"
        self.cursor.execute(sql,(id,))
        self.conn.commit()


    def update(self,name, phone, email, password,id):
        sql = "UPDATE users_detail SET name=%s, phone=%s, email=%s, password=%s WHERE id=%s"
        self.cursor.execute(sql, (name, phone, email, password, id))
        self.conn.commit()






