"""
효율적인 해킹 문제

>>N,M 이 주어지고 가장 많이 해킹할 수 있는 컴퓨터들을 출력하는 문제
>>N이 1만이하 M은 10만이하

"""
import sys
from collections import deque

INF=int(1e9)
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)

dis=[INF]*(n+1)

def bfs(start,graph):
    q=deque()
    visited=[False]*(len(graph))
    q.append(start)
    visited[start]=True
    count=0

    while q:
        now=q.popleft()
        for i in graph[now]:
            if not visited[i]:
                """
                왜 틀린걸까?
                if dis[i]<INF:
                    count+=dis[i]
                    visited[i]=True
                else:
                """

                q.append(i)
                visited[i]=True
                count+=1
    dis[start]=count


for i in range(1,n+1):
    bfs(i,graph)

max=-1
for i in range(1,n+1):
    if max<dis[i] and dis[i]<INF:
        max=dis[i]
for i in range(1,n+1):
    if max==dis[i]:
        print(i,end=' ')