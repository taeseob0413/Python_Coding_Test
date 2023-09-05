"""
유기농 배추 문제
"""
import sys
from collections import deque

input=sys.stdin.readline

t=int(input())

move_x=[-1,1,0,0]
move_y=[0,0,-1,1]


def bfs(graph, start):
    graph[start[0]][start[1]] = 0
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + move_x[i], y + move_y[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0


for _ in range(t):
    count=0
    n,m,bae=map(int,input().split())
    graph=[[0]*(m) for _ in range(n)]

    #배추 초기화
    for _ in range(bae):
        a,b=map(int,input().split())
        graph[a][b]=1

    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                count+=1
                bfs(graph,(i,j))

    print(count)




