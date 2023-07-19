"""
특정 거리의 도시 찾기(2번째)

1~N개의 도시가 존재하고 M개의 단방향 도로가 존재하고 모든 도로의 거리는 1일 때
출발 도시 X부터 거리가 K인 모든 도시들을 찾는 문제.

>>1.다익스트라로 풀기
>>2.DFS/BFS
"""
#1다익스트라를 이용한 풀이


import heapq
import sys

input=sys.stdin.readline
INF=1e9

n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
dis=[INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))

def dijkstra(start,k):
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

    result=[]
    for i in range(1,len(dis)):
        if dis[i]==k:
            result.append(i)
    return result

result=dijkstra(x,k)
if len(result)==0:
    print(-1)
else:
    for i in result:
        print(i)