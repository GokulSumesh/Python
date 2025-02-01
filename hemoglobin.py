a=input("Enter the Gender: ")
if a=="male":
    b=int(input("Enter the Age: "))
    if b>=12 and b<=18:
        c=int(input("Enter the Number: "))
        if c>=13.0 and c<=16.0:
            print("male healthy")
        else:
            print("male unhealthy")
    elif b>18:
        if c>=13.6 and c<=17.7:
            print("male healthy")
        else:
            print("male unhealthy")
    else:
        print("Not met the age")
elif a=="female":
    b=int(input("Enter the Age: "))
    if b>=12 and b<=18:
        c=int(input("Enter the Number: "))
        if c>=12.0 and c<=16.0:
            print("female healthy")
        else:
            print("female Unhealthy")
    elif b>18:
        if c>=12.1 and c<=16.1:
            print("female healthy")
        else:
            print("female unhaelthy")
    else:
        print("Not met the age")
elif a=="child":
    b=int(input("Enter the  months: "))
    b=int(input("Enter the  years: "))
    c=int(input("Enter the Number: "))
    if b<=1:
        c=int(input("Enter the Number: "))
        if c>=10.0 and c<=20.0:
            print("child healthy")
        else:
            print("child unhealty")
    elif b>1 and b<=2:
        if c>=10.0 and c<=11.2:
            print("child healthy")
        else:
            print("child unhealthy")
    elif b>2 and b<=6:
        if c>=9.5 and c<=14.5:
            print("child healthy")
        else:
            print("child unhealthy")
    elif b>0.5 and b<=2:
        if c>=10.5 and c<=13.5:
            print("child healthy")
        else:
            print("child unhealthy")
    elif b>=2 and b<=6:
        if c>=11.5 and c<=13.5:
            print("child healthy")
        else:
            print("child unhealthy")
    elif b>6 and b<=12:
        if c>=11.5 and c<=15.5:
            print("child healthy")
        else:
            print("child unhealthy")
    else:
        print("Not met the age")
else:
    print("Not applicable")