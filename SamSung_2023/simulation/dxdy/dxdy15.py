"""
주어진 길에서 더하기
"""
n,m=map(int,input().split())
strr=input()
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

dx,dy=[0,1,0,-1],[1,0,-1,0]
dir=3
x,y=n//2,n//2

result=graph[x][y]

for ope in strr:
    if ope=="L":
        dir=(dir+3)%4
    elif ope=="R":
        dir=(dir+1)%4
    else:
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<n and 0<=ny<n:
            result+=graph[nx][ny]
            x,y=nx,ny
print(result)