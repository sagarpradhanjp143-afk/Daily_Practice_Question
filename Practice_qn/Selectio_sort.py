
def Selsction_Sort(nums):
    n=len(nums)
    for i in range(0,n):
        mini_index=i
        for j in range(i+1,n):
            if nums[j]<nums[mini_index]:
                mini_index=j
                
                
        nums[i],nums[mini_index]=nums[mini_index],nums[i]

    return nums
    
print(Selsction_Sort([2,4,5,3,5,2,35,6]))
    
        
    

