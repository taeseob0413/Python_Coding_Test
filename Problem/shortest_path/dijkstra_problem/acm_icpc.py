"""
화성 탐사 문제
우선 이 문제를 다익스트라의 형태처럼 그래프를 재구현하면 풀기 쉬울듯.

"""
import heapq
INF=int(1e9)
t=int(input())


def dijkstra(start_x, start_y, n):
    dis = [[INF] * (n) for _ in range(n)]
    dis[start_x][start_y] = graph[start_x][start_y]
    q = []
    heapq.heappush(q, (dis[start_x][start_y], start_x, start_y))

    while q:
        dist, x, y = heapq.heappop(q)
        if dist > dis[x][y]:
            continue
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < dis[nx][ny]:
                    dis[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(dis[n - 1][n - 1])

for _ in range(t):
    n=int(input())
    graph=[]
    move_x=[1,-1,0,0]
    move_y=[0,0,1,-1]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    dijkstra(0,0,n)
