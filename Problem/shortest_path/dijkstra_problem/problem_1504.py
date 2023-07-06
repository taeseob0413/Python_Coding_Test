"""
특정한 최단 경로 문제

무방향그래프가 주어질 때 1번 정점에서 N번 정점으로의 최단거리를 구하는 문제이다.
두가지의 조건이 추가되는데

반드시 임의로 주어진 두 정점을 반드시 통과해야 한다는 것이다.

>>이 문제에서는 플로이드-워셜 알고리즘을 사용하면 문제가 풀리긴 하지만 노드의 개수가 최대 800개 이므로
>>O(V^3)의 시간복잡도를 갖는 플로이드-워셜로는 해결이 불가능 하다고 느꼈음.
>>따라서 O(ElogV)의 다익스트라 알고리즘을 2번사용하면 된다고 생각하였음.
"""
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,e=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

x,y=map(int,input().split())

def dijkstra(start,target,n):
    dis=[INF]*(n+1)
    dis[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue
        for i in graph[now]:
            cost=dis[now]+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return dis[target]

a=dijkstra(1,x,n)+dijkstra(x,y,n)+dijkstra(y,n,n)
b=dijkstra(1,y,n)+dijkstra(y,x,n)+dijkstra(x,n,n)

if a>=INF and b>=INF:
    print(-1)
else:
    print(min(a,b))

