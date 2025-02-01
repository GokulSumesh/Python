x=-123
if x < 0:
    a = str(x)[1:]  
    b = a[::-1]  
    c = int(b)  
    c=-c
        
else:
    a = str(x)  
    b = a[::-1] 
    c = int(b) 
            
if c>=-2**31 and c<=2**31-1:
    print(c)
else:
    print(0)








