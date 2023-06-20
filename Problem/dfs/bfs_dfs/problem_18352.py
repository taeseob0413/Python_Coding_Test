"""
특정 거리의 도시 찾기 문제

"""
import sys
from collections import deque

input=sys.stdin.readline
INF=int(1e9)

n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
dis=[INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

def bfs(start):
    q=deque([start])
    dis[start]=0
    while q:
        now=q.popleft()
        for i in graph[now]:
            #방문한 적이 있는 경우
            if dis[i]<dis[now]+1:
                continue
            dis[i]=dis[now]+1
            q.append(i)

bfs(x)
result=[]
for i in range(1,n+1):
    if dis[i]==k:
        result.append(i)
result.sort()
if len(result)==0:
    print(-1)
else:
    for i in result:
        print(i)