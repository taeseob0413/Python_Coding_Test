"""
백준 1753번 최단경로 문제

방향그래프가 주어질 때 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램

문제에서 특정 시작노드를 시작으로 하는 최단경로 문제이므로 다익스트라 사용
그 중에서 노드의 개수가 2만개이므로 O(ElogV)의 다익스트라 알고리즘을 사용한다.

문제에서 주의할 점은 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있다는 점이다.
"""
import sys
import heapq

INF=int(1e9)
input=sys.stdin.readline

v,e=map(int,input().split())
start=int(input())
graph=[[] for _ in range(v+1)]
dis=[INF]*(v+1)

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))


def dijkstra(start):
    q=[]
    dis[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue
        for i in graph[now]:
            cost=dis[now]+i[1]
            if dis[i[0]]>cost:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

for i in range(1,v+1):
    if dis[i]>=INF:
        print("INF")
    else:
        print(dis[i])
