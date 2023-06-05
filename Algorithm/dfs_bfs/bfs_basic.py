"""
bfs알고리즘은 큐를 이용하여 구현하는 그래프 탐색 알고리즘으로 시간 복잡도는 O(N)을 따른다.
또한 일반적인 코딩테스트에서 DFS보다는 시간복잡도 성능이 좋다.

동작 방법
1. 탐색 시작노드를 큐에 삽입한 뒤 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
"""
#bfs코드
from collections import deque

def bfs(visited,start,graph):
    visited[start]=True
    queue=deque([start])

    while queue:
        v=queue.popleft()
        print(v,end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[[0],[2,3,8],[1,7],[4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited=[False]*9

bfs(visited,1,graph)