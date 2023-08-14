"""
중량 제한 문제

>> 이 문제를 BFS or DFS 로 탐색을 할 경우에 모든 경로를 조사하는데 O(M)의 시간복잡도가 소요됨.
>> 하지만 문제는 이 중에서 경로의 무게중 최댓값을 구하기 위해서는 최대 O(N)의 시간복잡도가 소요되므로
>> 총 시간 복잡도는 O(NM)으로 시간 복잡도에 걸리게 된다.
>> 따라서 O(M)으로 모든 경로를 조사하면서 O(logC)로 경로의 최댓값을 구해주면 되는 문제이다.
"""
import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]


min_value=int(1e9)
max_value=1

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    if c>max_value:
        max_value=c
    if c<min_value:
        min_value=c

lo=list(map(int,input().split()))

def weight_limit(data,mid,lo):
    q=deque()
    visited = [False] * (n + 1)

    q.append(lo[0])
    visited[lo[0]]=True

    while q:
        now=q.popleft()
        for i in data[now]:
            if visited[i[0]]==False and i[1]>=mid:
                if i[0]==lo[1]:
                    return True
                else:
                    visited[i[0]]=True
                    q.append(i[0])
    return False

start=min_value
end=max_value

result=0
while start<=end:
    mid=(start+end)//2
    #경로가 존재 할 경우
    if weight_limit(graph,mid,lo)==True:
        start=mid+1
        result=mid
    else:
        end=mid-1

print(result)