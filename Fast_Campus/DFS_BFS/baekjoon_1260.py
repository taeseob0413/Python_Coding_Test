"""
DFS와 BFS의 출력 결과를 나타내기
O(N+M)의 시간 복잡도
"""
import sys
from collections import deque

input=sys.stdin.readline

n,m,start=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#O(N^2logN >> 10^6 * 10 >> 백만번의 연산 ok)
for i in range(1,n+1):
    graph[i].sort()

visited_dfs=[False]*(n+1)

def dfs(start,graph,visited):
    visited[start]=True
    print(start,end=' ')

    for i in graph[start]:
        if visited[i]!=True:
            dfs(i,graph,visited)


def bfs(start,graph):
    visited=[False]*(len(graph)+1)
    visited[start]=True
    q=deque()
    q.append(start)

    while q:
        now=q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if visited[i]!=True:
                visited[i]=True
                q.append(i)
dfs(start,graph,visited_dfs)
print()
bfs(start,graph)