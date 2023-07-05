"""
다익스트라 알고리즘 복습

출발 노드 설정 후 방문 처리 > 방문하지 않은 노드 중에 가장 짧은 거리의 노드 선택 > 방문 처리후 그 노드에서 갈 수 있는 방문하지 않은 노드의 최단 거리 결정
> 반복
"""
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
dis=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if dis[i]<min_value and not visited[i]:
            min_value=dis[i]
            index=i
    return index

def dijkstra(start):
    visited[start]=True
    dis[start]=0

    for i in graph[start]:
        dis[i[0]]=i[1]

    for i in range(n-1):
        now=get_smallest_node()
        visited[now]=True

        for j in graph[now]:
            cost=dis[now]+j[1]
            if dis[j[0]]>cost:
                dis[j[0]]=cost

dijkstra(start)

for i in range(1,n+1):
    if dis[i]==INF:
        print(-1)
    else:
        print(dis[i])