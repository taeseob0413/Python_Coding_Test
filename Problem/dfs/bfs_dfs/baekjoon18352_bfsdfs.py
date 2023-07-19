"""
18452번 문제를 BFS/DFS로 풀기
"""
from collections import deque

n,m,k,x=map(int,input().split())

graph=[[] for _ in range(n+1)]

dis=[-1]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b))

def bfs(start,k):
    dis[start]=0
    q=deque([start])

    while q:
        now=q.popleft()

        for i in graph[now]:
            if dis[i]==-1:
                q.append(i)
                dis[i]=dis[now]+1
    result=[]
    for i in range(1,len(dis)):
        if dis[i]==k:
            result.append(i)
    return result

result=bfs(x,k)
if len(result)==0:
    print(-1)
else:
    for i in result:
        print(i)