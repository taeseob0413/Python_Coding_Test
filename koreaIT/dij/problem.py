"""
다이스트라 1번

어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
하지만 X라는 도시에서 Y라는 도시로
"""
import heapq
import sys

INF = int(1e9)
input=sys.stdin.readline

n,m,start=map(int,input().split())
dis=[INF]*(n+1)
graph=[[] for _ in range(n+1)]

print(dis)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijk(start):
    dis[start]=0
    q=[]
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

sum=0
count=0

for i in range(len(dis)):
    if dis[i]>=INF or i ==start:
        continue
    else:
        print(dis[i])
        sum+=dis[i]
        count+=1

print(count,sum)