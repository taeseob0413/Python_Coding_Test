"""
백준 바이러스 문제
"""

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count=-1

def dfs(start,visited,graph):
    global count

    visited[start]=True
    count+=1

    for i in graph[start]:
        if not visited[i]:
            dfs(i,visited,graph)
visited=[False]*(n+1)
dfs(1,visited,graph)
print(count)
