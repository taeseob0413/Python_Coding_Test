"""
다익스트라 알고리즘 O(ElogV)
"""
import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
dis=[INF]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijk_ElogV(start):
    q=[]
    dis[start]=0
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dis[now]<dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]
            if dis[i[0]]>cost:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))


dijk_ElogV(start)


for i in range(1,n+1):
    if dis[i]==INF:
        print("경로 없어요.")
    else:
        print(dis[i])
