"""
숨바꼭질

N,M이 주어진다 (N은 헛간의 수, M은 통로의 수 , 통로는 양방향)

>>이 문제는 N,M이 각각 크므로 다익스트라를 이용하여 해결하여야 한다.
"""
import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

dis=[INF]*(n+1)

def dijk(start):
    q=[]
    dis[start]=0
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijk(1)
dis[0]=0

max_value=max(dis)
result=[]

for i in range(1,n+1):
    if dis[i]==max_value:
        result.append(i)
print(result[0], max_value, len(result))