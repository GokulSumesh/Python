
a=int(input("Enter the Value"))
if a>=0 and a<18:
    print("minor")
elif a>=18 and a<60:
    print("Major")
elif a>=60 and a<=118:
    print("Senoir Citizen")
else:
     print("No Age")