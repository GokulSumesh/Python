nums = [3,2,2,3]
val = 3
i=0
while i<len(nums):
    if nums[i]==val:
        nums.pop(i)
    else:
        i+=1
print(len(nums))

