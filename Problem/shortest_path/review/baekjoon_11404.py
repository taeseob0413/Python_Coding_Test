"""
플로이드 문제
N개의 도시가 존재(100이하)
M개의 버스가 존재(10만 이하)

모든 도시에서 다른 도시로 가는 최소 비용을 구하는 문제

>>N이 100이하 이므로 플로이드 워셜 알고리즘을 사용해도 된다.
>>또한 코드를 구현할 때 a 도시 b 도시가 존재할 때 이 둘을 잇는 도로가 여러개일 수도 있다는 점을 고려하면서 코드를 짜야함
"""
import sys

input=sys.stdin.readline
INF=int(1e9)

n=int(input())
m=int(input())

dis=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    dis[a][b]=min(dis[a][b],c)

for i in range(n+1):
    dis[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if dis[i][j]>=INF:
            print(0,end=' ')
        else:
            print(dis[i][j],end=' ')
    print()