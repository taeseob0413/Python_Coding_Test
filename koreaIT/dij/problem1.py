"""
다익스트라 2번
"""
import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

x,k=map(int,input().split())

def dijk(start,n):
    q=[]
    dis=[INF]*(n+1)
    dis[start]=0
    heapq.heappush(q,(0,start))


    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue

        for i in graph[now]:
            cost=i[1]+dist
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return dis

sum=dijk(1,n)[k]+dijk(k,n)[x]
if sum>=INF:
    print(-1)
else:
    print(sum)
