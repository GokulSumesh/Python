nums = [0,0,1,1,1,2,2,3,3,4]
i=0
while i<len(nums):
    j=i+1
    while j<len(nums):
        if nums[i]==nums[j]:
            nums.pop(j)
        else:
            j+=1
    i=i+1
print(len(nums))
    