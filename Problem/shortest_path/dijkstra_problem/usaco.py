"""
숨바꼭질

N개의 헛간이 주어지고 M개의 통로가 주어진다.
이때 최단거리가 가장 긴 헛간을 출력하고 최단거리, 같은 거리를 갖는 헛간의 개수 출력하기
"""
import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
dis=[INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a, 1))

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

dijkstra(1)
max_value=max(dis[1:])
count=0
max_index=0
#n~1까지의 인덱스
for i in range(n,0,-1):
    if dis[i]==max_value:
        max_index=i
        count+=1
print(max_index,max_value,count)