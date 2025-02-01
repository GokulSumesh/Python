# head = [1,1,2]
# n=len(head)
# for i in range(n):
#     for j in range(i+1,n-1): 
#         if head[i]==head[j]:
#             head.remove(head[j])
#         print(head)
            
head = [1,1,2,3,3]
n=len(head)
for i in range(n):
    for j in range(i+1,n-1): 
        if head[i]==head[j]:
            head.remove(head[j])
print(head)
