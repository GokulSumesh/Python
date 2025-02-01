# nums = [5,7,7,8,8,10]
# target = 8
# for i in range(len(nums)):
#     if target==nums[i]:
#         # print(i)
#         a=str(i)
#         b=list(a)
#         print(b,(b+1))
# else:
#     print(-1,-1)


nums = [5,7,7,8,8,10]
target = 8
for i in range(len(nums)):
    if target==nums[i]:
        a=i
        break
for j in range(len(nums)-1,-1,-1):
    if target==nums[j]:
        b=j
        break
print(a,b)

