"""
인구 이동 문제
"""
import sys
from collections import deque

input=sys.stdin.readline

n,l,r=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

move_x=[-1,1,0,0]
move_y=[0,0,1,-1]

def bfs(data,visited,l,r):
    result=[]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                sub=[]
                sum=data[x][y]
                q=deque()
                q.append((x,y))
                sub.append((x,y))
                visited[x][y]=True
                while q:
                    a,b=q.popleft()
                    for i in range(4):
                        nx,ny=a+move_x[i],b+move_y[i]
                        if 0<=nx<len(data) and 0<=ny<len(data) and not visited[nx][ny]:
                            if l<=abs(data[a][b]-data[nx][ny])<=r:
                                visited[nx][ny]=True
                                q.append((nx,ny))
                                sub.append((nx,ny))
                                sum+=data[nx][ny]
                result.append((sub,sum))
    if len(result)==len(data)*len(data):
        return False
    else:
        for locations,sum in result:
            avg=sum//len(locations)
            for a,b in locations:
                data[a][b]=avg
    return True

count=0
while True:
    visited = [[False] * (n) for _ in range(n)]
    if bfs(graph,visited,l,r)==False:
        break
    else:
        count+=1
print(count)