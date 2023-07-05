"""
플로이드 문제

모든 노드에서 모든 노드까지의 정보를 출력하는 문제이므로 플로이드 워셜 알고리즘을 사용하기에 적합하다
또한 노드의 갯수가 100개 이하이므로 O(V^3)의 플로이드 워셜 알고지금을 사용하여도 된다.
"""
INF=int(1e9)

n=int(input())
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=min(graph[a][b],c)


for i in range(1,n+1):
    graph[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]!=INF:
            print(graph[i][j],end=' ')
        else:
            print(0,end=' ')
    print()