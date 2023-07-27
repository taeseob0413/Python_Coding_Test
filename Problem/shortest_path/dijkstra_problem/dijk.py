"""
코드 복기
"""
import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

v,e=map(int,input().split())
start=int(input())
dis=[INF]*(v+1)
dis[0]=0
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    dis[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if dis[i[0]]>cost:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,v+1):
    print(dis[i],end=' ')
