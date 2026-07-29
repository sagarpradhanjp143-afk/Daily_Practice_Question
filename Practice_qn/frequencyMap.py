nums=[1,2,3,4,2,3,1,4,2,14,4,5,3,2,3]
hash_map={}
n=len(nums)
for i in range(0,n):
  hash_map[nums[i]]=hash_map.get(nums[i],0)+1

print(hash_map)