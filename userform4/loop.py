a=int(input("Enter the Number:"))
i=1
while i<=a:
    print(" "*(a-i),end="")
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    k=i-1
    while k>=1:
        print(k,end="")
        k-=1
    print()
    i+=1