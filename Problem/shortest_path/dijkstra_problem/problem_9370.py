"""
미확인 도착지 문제

어떤 예술가 한쌍의 출발지가 주어지고 도착지의 후보 2개가 주어진다.
또한 예술가 한쌍은 최단거리로 도착지의 후보들 중 하나로 갈 예정이다.
이때 예술가들이 지나간 길 한 곳이 주어질 때 목적지의 후보들 중 가능한 도착지를 구하여라.

>>이 문제의 경우에는 예술가들의 시작점부터 도착지 후보들까지의 최단거리와
>>주어진 지나간 길 한 곳을 포함한 최단거리가 같은 도착지의 후보들을 선정하는 문제이다.
>>우선 노드의 갯수가 2000개 이므로 O(V^3)의 플로이드 워셜 알고리즘 말고 다익스트라를 사용하기로 결정하였음.
>>100*50000*log2000  >> 11*100*50000=550000안에 풀 수 있음
"""
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

t=int(input())


def dijkstra(start,n,desti,graph):
    dis=[INF]*(n+1)
    q=[]
    dis[start]=0
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dis[now]<dist:
            continue
        for i in graph[now]:
            cost=dis[now]+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return dis[desti]

for _ in range(t):

    n,m,tt=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    target=[]
    start,x,y=map(int,input().split())
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    for _ in range(tt):
        target.append(int(input()))
    target.sort()
    for i in target:
        dis1=dijkstra(start,n,i,graph)
        dis2=dijkstra(start,n,x,graph)+dijkstra(x,n,y,graph)+dijkstra(y,n,i,graph)
        dis3=dijkstra(start,n,y,graph) + dijkstra(y,n,x,graph) + dijkstra(x,n,i,graph)
        if dis1==dis2 or dis1==dis3:
            print(i,end=' ')
    print()

