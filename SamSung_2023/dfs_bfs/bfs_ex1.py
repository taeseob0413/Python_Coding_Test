"""
K번 최댓값으로 이동하기
"""
from collections import deque

n,k=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

r,c=map(int,input().split())
cur_x,cur_y=r-1,c-1


dx,dy=[1,0,-1,0],[0,1,0,-1]
visited=[[False]*n for _ in range(n)]

def ini_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j]=False

def bfs(x,y,graph,target):
    move_points=[]
    q=deque()
    q.append((x,y))
    visited[x][y]=True

    while q:
        now_x,now_y=q.popleft()

        for i in range(4):
            nx,ny=now_x+dx[i],now_y+dy[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph):
                if not visited[nx][ny] and graph[nx][ny]<target:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    move_points.append((graph[nx][ny],nx,ny))
    ini_visited()
    return move_points


for i in range(k):
    result=bfs(cur_x,cur_y,graph,graph[cur_x][cur_y])

    if len(result)==0:
        print(cur_x+1,cur_y+1)
        break
    else:
        result.sort(key=lambda x:(-x[0],x[1],x[2]))
        cur_x,cur_y=result[0][1],result[0][2]

    if i==k-1:
        print(cur_x+1,cur_y+1)