
def LowerBound(nums,target):
  n=len(nums)
  ub=n
  low=0
  high=n-1
  while low<=high:
      mid=(low+high)//2
      if nums[mid]>target:
         lb=mid
         high=mid-1

      else:
         low=mid+1

  return ub

nums=[1,1,1,2,2,2,3,3,5,6,7,7,8,9,12,12,13]
target=50
print(LowerBound(nums,target))

