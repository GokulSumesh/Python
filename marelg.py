a=input("Enter the Gender: ")
b=int(input("Enter the Age: "))
if a=="male":
    if b>=21:
        print("male eligible for marriage")
    else :
        print("male not eligible for marriage")
elif a=="female":
    if b>=18:  
        print("female eligible for marriage")
    else :
        print("female not eligible for marriage")
else:
    print("not appplicable")