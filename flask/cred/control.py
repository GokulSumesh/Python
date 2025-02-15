import mysql.connector

class Login:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            db="flask"
        )
        self.con_cursor = self.con.cursor(dictionary=True)

    #for insert the table
    def insert(self,name,age):
        sql="insert into table1(name,age) values(%s,%s)"
        self.con_cursor.execute(sql,(name,age))
        return self.con.commit()
    
    #for select the table
    def select(self):
        sql="select * from table1"
        self.con_cursor.exeute(sql)
        return self.con_cursor.fetchall()
    
    #for select the table using id
    def select1(self,id):
        sql="select * from table1 where id=%s"
        self.con_cursor.execute(sql,(id))
        return self.con_cursor.fetchall()
    
    #for update the table
    def update(self,name,age,id):
        sql="update table1 set name=%s,age=%s where id=%s"
        self.con.cursor.execute(sql,(name,age,id))
        return self.con.commit()
    
    #for delete the table
    def delete(self,id):
        sql="delete from table1 whereid=%s"
        self.con.cursor.execute(sql,(id))
        return self.con.commit()
    
