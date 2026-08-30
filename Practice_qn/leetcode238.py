# nums=[0,3,1,4]
# n=len(nums)
# for i in range(0,n+1):
#     if i not in nums:
#         print(i)
def missing(nums):
    n=len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return i


print(missing(nums=[0,1,3,4]))