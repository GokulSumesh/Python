# nums1 = [1,3]
# nums2 = [2]
# nums3=nums1+nums2
# nums3.sort()
# a=len(nums3)/2
# b=int(a)
# print(float(nums3[b]))




# nums1 = [1,3]
# nums2 = [2]
# a=nums1+nums2
# a.sort()
# b=len(a)
# if b % 2 == 1:
#     print (a[b // 2])   
# else:
#     print ((a[b // 2 - 1] + a[b // 2]) / 2)  




# nums1 = [1,3]
# nums2 = [2,4]
# s=sorted(nums1+nums2)
# k=len(s)
# if k%2==0:
#     print((s[k//2]+s[(k//2)-1])/2)
# else:
#     print(s[k//2])




nums1 = [1,3]
nums2 = [2,4,5]
s=sorted(nums1+nums2)
k=len(s)
if k%2==0:
    print((s[k//2]+s[(k//2)-1])/2)
else:
    print(s[k//2])



 


