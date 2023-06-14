"""
미래도시 문제를 플로이드 워셜이 아닌 다익스트라로 풀기
"""
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

x,k=map(int,input().split())
def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,1))

    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)
cost1=distance[k]
distance=[INF]*(n+1)
dijkstra(k)
cost2=distance[x]

if cost1==INF or cost2==INF:
    print(-1)
else:
    print(cost1+cost2)