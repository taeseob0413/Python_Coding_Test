"""
커리 큘럼 문제

과목 N개와 각 과목의 수강시간 그리고 선수과목의 번호가 주어진다.
이때 강의는 한번에 여러개를 들을 수 있다.
각 과목을 다 듣는데 걸리는 시간을 구하기.

>>이 문제는 전형적인 위상정렬 문제이다. 또한 과목 여러개를 동시에 들을 수 있으므로 강의를 듣는 시간은 자신의 선수과목을 듣는 데 걸리는 시간에다가
자신의 시간만 더해주면 되는 문제이다.
"""
from collections import deque
import copy
n=int(input())
graph=[[] for _ in range(n+1)]
idg=[0]*(n+1)
cost=[0]*(n+1)

for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    cost[i]=tmp[0]
    for j in range(1,len(tmp)):
        if tmp[j]==-1:
            break
        else:
            graph[tmp[j]].append(i)
            idg[i]+=1

def topology_sort():
    q=deque()
    time=copy.deepcopy(cost)
    for i in range(1,n+1):
        if idg[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        for k in graph[now]:
            time[k] = max(time[k], time[now] + cost[k])
            idg[k]-=1
            if idg[k]==0:
                q.append(k)
    for i in range(1, n + 1):
        print(time[i])
topology_sort()
