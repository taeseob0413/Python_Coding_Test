"""
개선된 다익스트라 알고리즘.

"""
import heapq
import sys
INF=int(1e9)
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
start=int(input())
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        #방문한 경험이 있는 노드일 경우 pass
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("infinity")
    else:
        print(distance[i])


