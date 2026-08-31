nums=[7,2,1,5,6,4,8]
n=len(nums)
profit=0
maxi_profit=0
for i in range(0,n):
    for j in range(i+1,n):
        if nums[i]<nums[j]:
            profit=nums[j]-nums[i]
            maxi_profit=max(maxi_profit,profit)

print(maxi_profit)