"""
2020상반기 아기상어 문제
"""
from collections import deque

n=int(input())
graph=[]

fishes=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

a,b=0,0

for i in range(n):
    for j in range(n):
        if graph[i][j] in [1,2,3,4,5,6]:
            fishes.append((graph[i][j],i,j))
        elif graph[i][j] == 9:
            a,b=i,j

count=0
time=0
move_x=[-1,0,1,0]
move_y=[0,-1,0,1]
w=2


def bfs(a,b):
    visited=[[0]*n for _ in range(n)]
    cand=[]

    visited[a][b]=1
    q=deque()
    q.append((a,b))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+move_x[i],y+move_y[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==0 and graph[nx][ny]<=w:
                    visited[nx][ny]=visited[x][y]+1
                    if graph[nx][ny]==0 or graph[nx][ny]==w:
                        q.append((nx,ny))
                    else:
                        cand.append((visited[nx][ny]-1,nx,ny))
                        q.append((nx,ny))
    return cand

while True:
    candi=bfs(a,b)
    if len(candi)==0:
        break
    candi.sort(key=lambda x:(x[0],x[1],x[2]))
    time+=candi[0][0]
    count+=1
    if count==w:
        w+=1
        count=0
    graph[candi[0][1]][candi[0][2]]=9
    graph[a][b]=0
    a,b=candi[0][1],candi[0][2]


print(time)



