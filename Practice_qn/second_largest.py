nums=[-55,-32,-97,-99,-3,-67,45,6,7,88,8,99]
largest=float("-inf")
s_largest=float("-inf")
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])

for  i in range(0,n):
   if nums[i]>s_largest and nums[i]!=largest:
       s_largest=nums[i]

print(s_largest)