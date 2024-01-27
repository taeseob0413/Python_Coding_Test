"""
가운데에서 시작하여 빙빙돌기

>>가운데부터 시작하면 안되고 맨끝부터 생각을 해줘야함
"""

n=int(input())
graph=[[0]*n for _ in range(n)]

x,y=n-1,n-1
graph[x][y]=n*n
dir=2

dx,dy=[0,1,0,-1],[1,0,-1,0]

count=0
while True:
    nx,ny=x+dx[dir],y+dy[dir]
    if (0<=nx<n and 0<=ny<n) and graph[nx][ny]==0:
        graph[nx][ny]=graph[x][y]-1
        x,y=nx,ny
        count=0
    else:
        dir=(dir+1)%4
        count+=1
    if count>=4:
        break

for i in range(n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print()