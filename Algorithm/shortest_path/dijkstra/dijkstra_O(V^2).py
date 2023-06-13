"""
O(V^2)의 시간 복잡도를 갖는 다익스트라 알고리즘

방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택할 때 순차 탐색을 한다.
"""
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]

visit=[False]*(n+1)
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if not visit[i] and min_value>distance[i]:
            index=i
            min_value=distance[i]
    return index

def dijkstra(start):
    distance[start]=0
    visit[start]=True

    for i in graph[start]:
        distance[i[0]]=i[1]

    for j in range(n-1):
        now=get_smallest_node()
        visit[now]=True

        for i in graph[now]:
            cost=distance[now]+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("infinity")
    else:
        print(distance[i])
