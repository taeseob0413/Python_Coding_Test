"""
특정 거리의 도시 찾기 문제를 다익스트라를 통해서 구현하기
"""
import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,m,k,x=map(int,input().split())

#지도 list
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))

dis=[INF]*(n+1)

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

dijkstra(x)
flag=True
for i in range(1,n+1):
    if dis[i]==k:
        print(i)
        flag=False

if flag:
    print(-1)