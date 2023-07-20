"""
국경 문제
"""
from collections import deque

n,l,r=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

move_x=[1,-1,0,0]
move_y=[0,0,1,-1]

def bfs(graph,visited,start,l,r):
    result=[]
    x,y=start
    sum=graph[x][y]
    visited[x][y]=True
    q=deque()
    q.append((x,y))
    result.append((x,y))
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx,ny=a+move_x[i],b+move_y[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph):
                if l<=abs(graph[a][b]-graph[nx][ny])<=r and visited[nx][ny]==False:
                    q.append((nx,ny))
                    result.append((nx,ny))
                    sum+=graph[nx][ny]
                    visited[nx][ny]=True
    result.append(sum)
    if len(result)==2:
        return []
    else:
        return result
count=0
while True:
    visited=[[False]*(n) for _ in range(n)]
    total_list=[]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                sub=bfs(graph,visited,(i,j),l,r)
                if len(sub)!=0:
                    total_list.append(sub)
    if len(total_list)==0:
        break
    else:
       count+=1
       for i in total_list:
           sum=i[-1]
           avg=sum//(len(i)-1)
           for j in range(len(i)-1):
               x,y=i[j]
               graph[x][y]=avg
print(count)
