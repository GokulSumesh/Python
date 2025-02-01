# a=[1,2,3]
# b=['a','b','c']
# for i in b:
#     a.append(i)
# print(a)


# a=[1,2,3]
# b=['a','b','c']
# i=0
# while i in b:
#     a.append(i)
# print(a)



# a=[1,2,3,4,5,6,7]
# b=0
# for i in a:
#     b=b+i
# print(b)


# a=[8,7,5,3,2]
# target=9
# i=0
# while i<len(a):
#     j=i+1
#     while j<len(a):
#         if a[i]+a[j]==target:
#             print(a[i],a[j])
#         j+=1
#     i+=1


# a=[8,7,5,3,2]
# target=9
# i=0
# second=0
# while i<len(a):
#     second=target-a[i]
#     try:
#         index2=a.index(second)
#         if index2 :
#             print(a[i],second)
#     except:
#         print("index not found")
#     i+=1



# a=[1,2,3,4,5,6,7]
# b=0
# for i in a:
#     b=b+i
# print(b)



# a=['a','b','c','d','e']
# b=input("Enter the Number :")

# for i in range(len(a)):
#     if a[i]==b:
#         print(i)
# i+=1

# a=[1,2,3,4,5]
# for i in range(len(a)):
#     print(a)

# a=int(input("Enter the Number :"))
# b=1
# c=11
# for i in range(b,c):
#     print(b,"*",a,"=",b*a)
#     b+=1



# a=int(input("Enter the Number :"))
# b=10

# for i in range(1,b+1):
#     print(i,"*",a,"=",i*a)
#     b+=1

# a=int(input("Enter the Number :"))
# b=1
# c=10
# for i in range(b,c+1):
#     if a%2==0:
#         print(b,"*",a,"=",b*a)
#         b+=1
#     else:
#         print(c,"*",a,"=",c*a)
#         c-=1

# a=int(input("Enter the Number :"))
# b=10
# for i in range(1,b+1):
#     if a%2==0:
#         print(i,"*",a,"=",i*a)
#         b+=1
#     else:
#         print(b,"*",a,"=",b*a)
#         b-=1



a=[8,7,5,3,2]
target=9
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]+a[j]==target:
            print(i,j)
        j+=1
    i+=1









  
    
