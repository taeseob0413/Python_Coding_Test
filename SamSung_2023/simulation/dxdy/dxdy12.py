"""
빙빙 돌며 숫자 사각형 채우기 2

>>반시계 방향 회전
"""

n,m=map(int,input().split())
graph=[[0]*m for _ in range(n)]

x,y=0,0
graph[x][y]=1
dir=1

dx,dy=[0,1,0,-1],[1,0,-1,0]

count=0
while True:
    nx,ny=x+dx[dir],y+dy[dir]
    if (0<=nx<n and 0<=ny<m) and graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]+1
        x,y=nx,ny
        count=0
    else:
        dir=(dir+3)%4
        count+=1

    if count>=4:
        break

for i in range(n):
    for j in range(m):
        print(graph[i][j],end=' ')
    print()
