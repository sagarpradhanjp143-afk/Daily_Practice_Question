# nums=[[1,2,3],[2,3,4],[4,6,7]]
# rows=len(nums)
# colm=len(nums)
# for i in range(0,rows):
#     for j in range(0,colm):
#        print(nums[1][2],end=" ")
# print()

nums=[[1,2,3],[2,3,4],[4,6,7]]
rows=len(nums)
colm=len(nums)
for i in range(0,rows):
    for j in range(0,colm):
        if j==i:
            print(nums[i][j],end=" ")
print()