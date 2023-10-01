"""
다익스트라 알고리즘 O(V^2) 구현
"""
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
dis=[INF]*(n+1)
visited=[False]*(n+1)

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    #a에서 b로 가는 비용이 c인 경우
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    index=0

    for i in range(1,n+1):
        if not visited[i] and dis[i]<min_value:
            min_value=dis[i]
            index=i
    return index

def dijkvv(start):
    dis[start]=0
    visited[start]=True

    for i in graph[start]:
        dis[i[0]]=i[1]

    for _ in range(n-1):
        now=get_smallest_node()
        visited[now]=True
        for j in graph[now]:
            cost=dis[now]+j[1]
            if dis[j[0]]>cost:
                dis[j[0]]=cost


dijkvv(start)


for i in range(1,n+1):
    if dis[i]==INF:
        print("경로 없어요.")
    else:
        print(dis[i])
