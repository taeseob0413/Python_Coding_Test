"""
화성 탐사 문제
"""
import sys
import heapq

INF=int(1e9)
input=sys.stdin.readline

t=int(input())

move_x=[-1,1,0,0]
move_y=[0,0,-1,1]

def dijk(num,gra):
    dis=[[INF]*(num) for _ in range(num)]
    q=[]
    dis[0][0]=gra[0][0]
    heapq.heappush(q,(dis[0][0],(0,0)))

    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now[0]][now[1]]:
            continue

        for i in range(4):
            nx,ny=now[0]+move_x[i],now[1]+move_y[i]
            if 0<=nx<num and 0<=ny<num:
                cost=dist+gra[nx][ny]
                if cost<dis[nx][ny]:
                    dis[nx][ny]=cost
                    heapq.heappush(q,(cost,(nx,ny)))
    return dis[num-1][num-1]

for _ in range(t):
    n=int(input())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    print(dijk(n,graph))