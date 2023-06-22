"""
경쟁적 전염
NXN의 시험관이 주어지고 K종류의 바이러스가 주어진다.   (1<=N<=200, 1<=K<=1000)
각 바이러스는 1초동안에 상하좌우로 전염되어 나간다. 바이러스의 전염은 바이러스의 번호가 낮은 순으로 전염되어 진다.

각 초 동안에 바이러스가 한번씩 동등한 기회를 부여 받아야 하므로 BFS로 문제 풀기 시작
N과 K가 작은 수여서 우선 시간복잡도는 크게 고려 X
"""
from collections import deque

n,k=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
s,a,b=map(int,input().split())

virus=[]

#바이러스의 정보를 담기 / 바이러스의 종류(1~K), 위치 정보 담기
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            virus.append((graph[i][j],i,j,0))
virus.sort(key=lambda x:x[0])
move_x=[1,-1,0,0]
move_y=[0,0,1,-1]


q=deque()

for i in virus:
    q.append(i)

while q:
    vir,x,y,time=q.popleft()
    for i in range(4):
        nx=x+move_x[i]
        ny=y+move_y[i]
        if 0<=nx<n and 0<=ny<n and time<=s-1:
            if graph[nx][ny]==0:
                graph[nx][ny]=vir
                q.append((vir,nx,ny,time+1))

print(graph[a-1][b-1])