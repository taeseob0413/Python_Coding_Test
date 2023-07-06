"""
숨바꼭질 3

수빈이와 동생의 좌표가 주어지고 수빈이는 매 순간 x-1,x+1,x*2의 위치로 갈 수 있다.
수빈이가 동생을 찾는 가장 적게 걸리는 시간은??

>>이 문제는 수직선 문제이므로 DP를 적절하게 사용하면 풀 수 있을 것 같음.
"""
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
dis=[INF]*(100001)


def shortest_path(start):
    dis[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dist>dis[now]:
            continue

        if now-1>=0:
            nx=now-1
            if dis[nx]>dis[now]+1:
                dis[nx]=dis[now]+1
                heapq.heappush(q,(dis[nx],nx))
        if now+1<=100000:
            nx=now+1
            if dis[nx] > dis[now] + 1:
                dis[nx] = dis[now] + 1
                heapq.heappush(q, (dis[nx], nx))
        if now*2<=100000:
            nx=now*2
            if dis[nx]>dis[now]:
                dis[nx]=dis[now]
                heapq.heappush(q,(dis[nx],nx))

shortest_path(n)
print(dis[m])