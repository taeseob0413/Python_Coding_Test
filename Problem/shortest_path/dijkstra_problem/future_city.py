"""
미래도시 문제
"""
import sys
INF=int(1e9)
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b],graph[b][a]=1,1

x,k=map(int,input().split())

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
if graph[1][k]+graph[k][x]<INF:
    print(graph[1][k]+graph[k][x])
else:
    print(-1)