"""
정수 삼각형
"""

n=int(input())
num_list=[]
d=[]
for _ in range(n):
    num_list.append(list(map(int,input().split())))
    d.append([0]*(n+1))
d[0][0]=num_list[0][0]
for i in range(n-1):
    for j in range(i+1):
        d[i+1][j]=max(d[i+1][j],d[i][j]+num_list[i+1][j])
        d[i+1][j+1]=max(d[i+1][j+1],d[i][j]+num_list[i+1][j+1])
print(max(d[n-1]))