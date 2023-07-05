"""
전보 문제
"""
import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,m,start=map(int,input().split())

graph=[[] for _ in range(n+1)]
dis=[INF]*(n+1)

for _ in range(m):
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
            cost=dis[now]+i[1]
            if dis[i[0]]>cost:
                dis[i[0]]=cost
                heapq.heappush(q,(dist,i[0]))

dijkstra(start)
max_num=0
count=0
for i in dis:
    if i>=INF:
        continue
    else:
        count+=1
        if max_num<i:
            max_num=i

print(count-1,max_num)
