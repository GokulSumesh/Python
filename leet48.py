a = [[1,2,3],[4,5,6],[7,8,9]]
n=len(a)
for i in range(n):
    for j in range(i,n):
        a[i][j],a[j][i]=a[j][i],a[i][j]
for k in a:
    k.reverse()
print(a)




         
