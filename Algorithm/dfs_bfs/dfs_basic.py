"""
dfs는 깊이 우선으로 그래프를 탐색하는 알고리즘이다. 스택과 재귀함수를 이용하여 구현한다.

dfs의 탐색방식은 다음과 같다

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있을 때 인접 노드를 스택에 넣은 뒤 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
"""

#dfs 코드
def dfs(visited,v,graph):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(visited,i,graph)

graph=[[0],[2,3,8],[1,7],[4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited=[False]*9

dfs(visited,1,graph)