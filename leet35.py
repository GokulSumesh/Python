Input: nums = [1,3,5,6]
target = 5
for i in range(len(nums)):
    if target not in nums:
        nums.append(target)
        nums.sort()
for i in range(len(nums)):
    if target==nums[i]:
        print(i)