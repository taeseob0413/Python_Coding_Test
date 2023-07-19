"""
경쟁적 전염 2회독
"""
from collections import deque

n,k=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
s,x,y=map(int,input().split())

#초기 바이러스를 담을 리스트
virus=[]
#O(N^2)
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            virus.append((graph[i][j],i,j,0))

#바이러스를 순서대로 정렬 O(N^2)
virus.sort(key=lambda x:x[0])

q=deque()
for i in range(len(virus)):
    q.append(virus[i])

move_x=[-1,1,0,0]
move_y=[0,0,1,-1]

while q:
    vir,dx,dy,time=q.popleft()
    if time>=s:
        break
    for i in range(4):
        nx=dx+move_x[i]
        ny=dy+move_y[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=vir
                q.append((vir,nx,ny,time+1))

print(graph[x-1][y-1])