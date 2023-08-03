"""
화성 탐사 문제
NxN의 지도가 주어질 때 0,0 에서 N-1,N-1 까지의 최단 경로를 구하는 문제(N은 125이하)

>>이 문제는 BFS로 풀어도 되고 프로이드 워셜로 풀어도 되고 다익스트라로 풀어도 가능하다.
"""
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

t=int(input())

move_x=[-1,1,0,0]
move_y=[0,0,-1,1]


def dijk(graph, dis):
    start = (0, 0)
    q = []
    dis[start[0]][start[1]] = graph[start[0]][start[1]]
    heapq.heappush(q, (dis[start[0]][start[1]], start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > dis[now[0]][now[1]]:
            continue
        for i in range(4):
            nx, ny = now[0] + move_x[i], now[1] + move_y[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                cost = dis[now[0]][now[1]] + graph[nx][ny]
                if cost < dis[nx][ny]:
                    dis[nx][ny]=cost
                    heapq.heappush(q, (cost, (nx, ny)))
    print(dis[len(graph)-1][len(graph)-1])

for _ in range(t):
    n=int(input())
    dis=[[INF]*(n) for _ in range(n)]
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    dijk(graph,dis)
