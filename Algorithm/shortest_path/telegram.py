"""
전보 문제

도시의 개수 N과 통로의 개수 M 시작 도시 C가 주어질 때
C에서 최대한 많은 도시로 전보를 보내고자 한다. 전보를 보낼 수 있는 도시의 개수와 이때의 메시지가 전달되는 시간을 구하는 문제

1<=N<=30000, 1<=M<=200000 , 1<=C<=N

이 문제는 N과 M이 크기 때문에 다익스트라 알고리즘으로 풀면 된다.
시작점으로 부터의 거리 리스트에서 INF와 0이 되는 노드를 제외한 노드들을 카운트하여 합을 구하면 되는 문제
"""
import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
max=0
count=0
for i in range(1,n+1):
    if distance[i] != 0 and distance != INF:
        if max<distance[i]:
            max=distance[i]
        count+=1
print(count, max)