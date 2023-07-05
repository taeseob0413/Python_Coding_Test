"""
다익스트라 O(ElogV)코드 복습

다익스트라에서 매 단계에서 가장 짧은 거리의 원소를 선택할 때 heapq 자료구조를 사용하도록 한 것.
"""
import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
dis=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    dis[start]=0
    q=[]
    #heapq는 삽입하는 첫번째 원소를 우선순위로 하기 때문에 (거리,노드) 순으로 삽입을 해야함
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dis[now]<dist:
            continue

        for i in graph[now]:
            cost=dis[now]+i[1]
            if dis[i[0]]>cost:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in dis:
    print(i)
