nums=[2,3,4,5,6,78,5,43,3]
n=len(nums)
for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        print(False)

print(True)