matrix=[[4,3,2,1],
        [6,2,5,0],
        [7,8,9,10],
        [2,3,0,7]]

r=len(matrix)
c=len(matrix)
rowt=[0 for _ in range(r)]
colmt=[0 for _ in range(c)]
for i in range(0,r):
    for j in range(c):
        if matrix[i][j]==0:
            rowt[i]=-1
            colmt[j]=-1

for i in range(0,r):
    for j in range(c):
        if rowt[i]==-1 or colmt[j]==-1:
            matrix[i][j]=0

print(matrix)