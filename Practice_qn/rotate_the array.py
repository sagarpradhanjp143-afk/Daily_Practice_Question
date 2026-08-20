# nums=[5,7,8,9,3,2,4,5,6,1]
# n=len(nums)
# temp=nums[n-1]
# for i in range(n-2,-1,-1):
#     nums[i+1]=nums[i]

# nums[0]=temp

# print(nums)

def RotateArray(nums):
    n=len(nums)
    temp=nums[n-1]

    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]

    nums[0]=temp

    return nums

nums=[5,7,8,9,3,2,4,5,6,1]

print(RotateArray(nums))