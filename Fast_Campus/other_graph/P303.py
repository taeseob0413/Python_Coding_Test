"""
커리큘럼 문제

>>위상 정렬 문제
>>이 문제에서의 핵심은 자신으로 오는 간선들 중에 가장 큰 값의 가중치가 필요
"""
from collections import deque
import sys

input=sys.stdin.readline

n=int(input())
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
#가중치를 기록하기 위한 테이블
dis=[0]*(n+1)
result=[0]*(n+1)
for i in range(n):
    num_list=list(map(int,input().split()))
    dis[i+1]=num_list[0]
    for j in range(1,len(num_list)):
        if num_list[j]==-1:
            break
        else:
            indegree[i+1]+=1
            graph[num_list[j]].append(i+1)

q=deque()

for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
        result[i]=dis[i]
while q:
    now=q.popleft()

    for i in graph[now]:
        indegree[i]-=1
        result[i]=max(result[i],result[now]+dis[i])
        if indegree[i]==0:
            q.append(i)


print(indegree)
for i in range(1,n+1):
    print(result[i])