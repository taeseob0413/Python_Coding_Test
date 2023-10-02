"""
정확한 순위

N=500, M=10000(성적 비교 횟수)가 주어질 때 정확하게 성적을 비교할 수 있는 학생을 출력하는 문제

>> 이 문제는 M번의 비교에서 A>B일 경우 B->A로 경로를 설정하면 된다.
>> 시간제한이 5초 이므로 1억번의 연산을 한다고 할 때 O(N^3)까지 가능하므로 플로이드 워셜 알고리즘을 사용하면 좋을 듯 하다.
>> 이때 A라는 노드에서 도착할 수 있는 갯수(자신보다 높은 등수) + 자신으로 도착할 수 있는 노드의 갯수(자신보다 낮은 등수) =N-1일 경우에 A는 정확하게 등수를 예측할 수 있다.
>> A가 B보다 작으면서 B가 A보다 작은 경우는 존재하지 않으므로 사이클은 고려하지 않아도 된다.
"""
import sys

INF=int(1e9)
input=sys.stdin.readline

n,m=map(int,input().split())
result=0

dis=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dis[i][i]=0

for _ in range(m):
    a,b=map(int,input().split())
    dis[a][b]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])

for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if dis[i][j]!=0 and dis[i][j]<INF:
            count+=1
        if dis[j][i]!=0 and dis[j][i]<INF:
            count+=1
    if count==n-1:
        result+=1
print(result)
