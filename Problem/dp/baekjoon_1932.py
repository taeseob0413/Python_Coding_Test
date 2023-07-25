"""
정수 삼각형 문제
"""
import copy
n=int(input())

tri=[]
for _ in range(n):
    tri.append(list(map(int,input().split())))

d=copy.deepcopy(tri)

for i in range(n-1):
    for j in range(len(tri[i])):
        d[i+1][j]=max(d[i+1][j],d[i][j]+tri[i+1][j])
        d[i+1][j+1]=max(d[i+1][j+1],d[i][j]+tri[i+1][j+1])

print(max(d[n-1]))
