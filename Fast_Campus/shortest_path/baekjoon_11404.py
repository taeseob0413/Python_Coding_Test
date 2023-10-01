"""
플로이드 문제
N개의 도시가 주어지고 한 도시에서 출바하여 다른 도시에 도착하는 M개의 버스가 존재
A에서 B로 갈때의 비용의 최솟값을 구하는 문제

>>N이 100개이므로 플로이드 워셜로 풀수 있음
>>기본 문제와 다른 점은 시작 도시와 도착 도시를 이동하는 버스가 여러대 있을 수 있다는 점이 다른점임.
>>그래프에서 비용을 입력할 때 가장 작은 값을 입력을 해줘야함.
"""
import sys

input=sys.stdin.readline
INF=int(1e9)

n=int(input())
m=int(input())

dis=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dis[i][i]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    dis[a][b]=min(dis[a][b],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dis[i][j]>=INF:
            print(0,end=" ")
        else:
            print(dis[i][j],end=' ')
    print()