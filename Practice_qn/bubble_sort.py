nums=[1,6,4,5,9,8,10,12,14,3]
n=len(nums)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]

print(nums)


