"""
커리큘럼 문제
총 N개의 과목의 선수과목과 강의시간이 주어진다.(N<=500)
이때 N개의 강의를 듣을 때 걸리는 최소 시간 구하기
"""

from collections import deque

v=int(input())
graph=[[] for _ in range(v+1)]
indegree=[0]*(v+1)
lec_time=[0]*(v+1)
result_time=[0]*(v+1)
for i in range(1,v+1):
    lec=list(map(int,input().split()))
    lec_time[i]=lec[0]
    if len(lec)>2:
        for j in range(1,len(lec)):
            if lec[j]!=-1:
                indegree[i]+=1
                graph[lec[j]].append(i)
def topology_sort():
    q=deque()
    #초기 설정
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
            result_time[i]=lec_time[i]

    while q:
        now=q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            result_time[i] = max(result_time[i], lec_time[i] + result_time[now])
            if indegree[i]==0:
                q.append(i)
topology_sort()
for i in range(1,v+1):
    print(result_time[i])


