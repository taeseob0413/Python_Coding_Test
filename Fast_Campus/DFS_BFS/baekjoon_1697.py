"""
숨바꼭질 문제

"""
import sys
from collections import deque

INF=int(1e9)
input=sys.stdin.readline

n,k=map(int,input().split())
dis=[INF]*(100001)

q=deque()
q.append(n)
dis[n]=0

while q:
    now=q.popleft()
    if now==k:
        print(dis[now])
    if now-1>=0:
        if dis[now-1]>dis[now]+1:
            q.append(now-1)
            dis[now - 1]=dis[now]+1
    if now+1<=100000:
        if dis[now+1]>dis[now]+1:
            q.append(now+1)
            dis[now+1]=dis[now]+1
    if now*2<=100000:
        if dis[now*2]>dis[now]+1:
            q.append(now*2)
            dis[now*2]=dis[now]+1