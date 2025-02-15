a=open("demofile.txt", "w")
a.write("|---------------------------------------------------------------------------|\n|       Name     |       Age     |      Phone     |           Email         |\n|---------------------------------------------------------------------------|\n")
for i in range (0,1,+1):
    name=input("Enter the name: ")
    age=(input("Enter the Age: "))
    phone=(input("Enter the Phone: "))
    email=input("Enter the Email: ")
    data="|"+"      "+name+"            "+age+"            "+phone+"            "+email+"         |"+"\n"
    a.write(str(data))


a=open("demofile.txt", "r")
b=a.readlines()
for i in range(len(b)):
    print(b[i])



