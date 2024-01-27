"""
빙빙돌며 숫자 채우기 문제
"""

n,m=map(int,input().split())
graph=[[0]*m for _ in range(n)]

dx,dy=[0,1,0,-1],[1,0,-1,0]

x,y=0,0
dir=0

graph[x][y]=1
count=0

while True:
    if count>=4:
        break
    nx,ny=x+dx[dir],y+dy[dir]
    if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        x,y=nx,ny
        count=0

    else:
        dir=(dir+1)%4
        count+=1

for i in range(n):
    for j in range(m):
        print(graph[i][j],end=" ")
    print()