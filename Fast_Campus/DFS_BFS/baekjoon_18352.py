"""
백준 18352 - 특정 거리의 도시 찾기 문제

X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력하는 문제.
이때 최단 거리가 K인 도시가 하나도 없을 경우 -1 출력

>>이 문제는 다익스트라와 BFS로 풀 수 있다.
>>두 가지 방법 모두 시간복잡도는 만족
"""
import sys
from collections import deque

input=sys.stdin.readline

n,m,k,x=map(int,input().split())

#지도 list
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

#BFS를 이용한 풀이
visited=[False]*(n+1)
result=[]
q=deque()
q.append((x,0))
visited[x]=True

while q:
    now,dis=q.popleft()

    if dis==k:
        result.append(now)
    for i in graph[now]:
        if visited[i]==False:
            q.append((i,dis+1))
            visited[i]=True

if len(result)==0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)