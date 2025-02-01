nums = [1, 2, 0]
nums.sort()
a = 1
for i in range(len(nums)):
    if nums[i] > 0:  
        if nums[i] == a:
            a += 1
        elif nums[i] > a:
            break
print(a)


nums = [3,4,-1,1]
nums.sort()
a = 1
for i in range(len(nums)):
    if nums[i] > 0:  
        if nums[i] == a:
            a += 1
        elif nums[i] > a:
            break
print(a)


nums = [7,8,9,11,12]
nums.sort()
a = 1
for i in range(len(nums)):
    if nums[i] > 0:  
        if nums[i] == a:
            a += 1
        elif nums[i] > a:
            break
print(a)
