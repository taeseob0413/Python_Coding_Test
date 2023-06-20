"""
연구소 문제
"""
import sys
from collections import deque
from itertools import combinations

input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

brick=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            brick.append((i,j))

check_brick=list(combinations(brick,3))

move_x=[-1,1,0,0]
move_y=[0,0,-1,1]

def bfs(start_x,start_y,graph):
    q=deque()
    q.append((start_x,start_y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+move_x[i]
            ny=y+move_y[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
                if graph[nx][ny]==0:
                    graph[nx][ny]=2
                    q.append((nx,ny))
max_count=0
sub_graph=[[0]*m for _ in range(n)]

for bricks in check_brick:
    for k in range(n):
        for j in range(m):
            sub_graph[k][j]=graph[k][j]
    t1,t2,t3=bricks
    sub_graph[t1[0]][t1[1]],sub_graph[t2[0]][t2[1]],sub_graph[t3[0]][t3[1]]=1,1,1
    count=0
    for i in range(n):
        for j in range(m):
            if sub_graph[i][j]==2:
                bfs(i,j,sub_graph)
    for i in range(n):
        for j in range(m):
            if sub_graph[i][j]==0:
                count+=1
    max_count=max(count,max_count)

print(max_count)



