import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user= "root",
    password = "admin123",
    database  = "user"
)

cor = conn.cursor(dictionary = True)

cor.execute("select * from snacks")
users=cor.fetchall()
print(users)
# for user in users:
#     print (user["price"])