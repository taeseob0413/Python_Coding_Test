"""
플로이드 워셜 알고리즘 : 모든 노드에서 다른 모든 노드까지의 최단 거리를 구하는 데 사용하는 알고리즘 / 동적 계획법 사용 / O(N^3)
다익스트라 알고리즘 : 특정 노드에서 시작하여 다른 노드들 까지의 최단 거리 or 특정 목적지까지의 최단 거리를 구할 때 사용 / 그리디 알고리즘 / O(ElogV)

플로이드 워셜 알고리즘은 구현하기에는 쉽지만 아이디어를 잘 이해하고 있어야 한다.

플로이드 워셜 알고리즘의 아이디어는 노드 N개가 주어질 때
1번 노드부터 시작하여 N번 노드까지 자신을 거쳐가는 경로를 생각해 주는 문제이다

만약 1번 노드를 거쳐간 경로를 생각할 때 자신을 제외한 n-1개의 노드에서 2개를 고르고 방향을 고려한다.
만약 a,b와 1번 노드를 생각할 때 Dab= min(Dab,Da1+D1b)로 점화식을 세울 수 있음.
"""
import sys
input=sys.stdin.readline
INF=int(1e9)

n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print("INF",end=' ')
        else:
            print(graph[i][j],end=' ')
    print()