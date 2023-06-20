"""
미로탈출 문제
NXM의 미로가 주어지고 시작점은 (1,1)이고 끝점은 (N,M)이다.
이때 미로를 탈출할 수 있는 최단거리를 구하자.
이때 노드를 방문할 떄는 반드시 1인 경우에만 방문 >> 최단거리 문제이므로

나중에 다익스트라로도 풀 수 있는 문제.
"""
from collections import deque

move_x=[-1,1,0,0]
move_y=[0,0,-1,1]

def bfs(start_x,start_y,graph):
    q=deque()
    q.append([start_x,start_y])

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+move_x[i]
            ny=y+move_y[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
                if graph[nx][ny]==1:
                    graph[nx][ny]=1+graph[x][y]
                    q.append([nx,ny])

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

bfs(0,0,graph)
print(graph[n-1][m-1])