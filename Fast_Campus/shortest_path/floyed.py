"""
플로이드 워셜 알고리즘
"""
import sys

INF=int(1e9)
input=sys.stdin.readline

n,m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print("경로 없음",end=" ")
        else:
            print(graph[i][j],end=" ")
    print()