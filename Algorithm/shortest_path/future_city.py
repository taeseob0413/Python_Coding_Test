"""
미래 도시 문제
도시의 개수 N,간선의 개수 M이 주어진다.
이 때 두 도시를 잇는 간선은 양방향으로 움직이는 것이 가능하다.

회사원 A는 1번 도시를 출발하여 소개팅을 하는 장소 K를 들렸다가 최종 미팅장소인 X로 가야한다.
이때 최단거리를 구하는 문제

우선 이 문제는 플로이드 워셜과 다익스트라 둘 다 가능하다
N이 100이므로 O(N^3)의 시간복잡도인 플로이드 워셜을 사용하였을 경우에도 시간 초과가 발생하지 않는다.
플로이스 워셜을 사용하였을 경우에는 graph[1][k]+graph[k][x]를 하면 된다.

만약 다익스트라를 사용하는 경우에는 출발점을 1번 한번 K번 한번으로 하여 구할 수 있을 듯하지만
중간에 distance리스트를 다시 초기화 해줘야 할 듯 하다.
"""

#1 플로이드 워셜 알고리즘을 사용하여 문제 풀기.
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b],graph[b][a]=1,1

x,k=map(int,input().split())

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
if graph[1][k]==INF or graph[k][x]==INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])
