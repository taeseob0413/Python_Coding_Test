"""
운동

V개의 마을과 E개의 도로가 주어진다.
이때 운동경로 사이클 찾는 문제
V가 400이므로 64*10^6= 640만의 시간 복잡도를 갖는 플로이드 워셜 알고리즘으로 풀 수 있음.
"""
import sys

INF=int(1e9)
input=sys.stdin.readline

v,e=map(int,input().split())
graph=[[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for i in range(1,v+1):
    graph[i][i]=0

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

min_value=INF

for i in range(1,v+1):
    for j in range(1,v+1):
        if i==j:
            continue
        else:
            if min_value>graph[i][j]+graph[j][i]:
                min_value=graph[i][j]+graph[j][i]

if min_value>=INF:
    print(-1)
else:
    print(min_value)