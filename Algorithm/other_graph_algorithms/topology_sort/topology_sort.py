"""
위상 정렬 알고리즘
>> 순서가 정해져 있는 일련의 작업을 차례대로 수행할 때 사용하는 알고리즘(방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것)
ex)선수과목이 있는 학습 순서 설정.
>> 진입차수를 고려하여 구현(진입차수 : 어떤 특정 노드로 들어오는 간선의 개수)

구현 순서
1. 진입 차수가 0인 노드를 큐에 넣는다.
2. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
3. 2번 과정의 간선 제거 후 새롭게 진입 차수가 0이된 노드를 큐에 넣는다

O(V+E)의 시간 복잡도를 갖는다.
"""
from collections import deque

v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
indegree=[0]*(v+1)

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque()
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i,end=' ')
topology_sort()
