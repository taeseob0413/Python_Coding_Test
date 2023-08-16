"""
BFS 리뷰

>> BFS는 너비 우선 탐색 알고리즘으로 큐 자료구조를 사용한다.
>> 시간 복잡도는 O(N)을 따르고 일반적으로 DFS보다 시간복잡도에서 좋은 편이다.
>> 최단 경로 문제에서도 자주 사용됨.
"""
from collections import deque

def bfs(data,visited,start):
    visited[start]=True
    q=deque([start])

    while q:
        now=q.popleft()
        print(now,end=" ")
        for i in data[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True


graph=[[0],[2,3,8],[1,7],[4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited=[False]*9

bfs(graph,visited,1)