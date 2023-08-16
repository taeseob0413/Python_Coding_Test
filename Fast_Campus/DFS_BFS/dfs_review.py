"""
dfs 복습

깊이 우선 탐색 알고리즘 , 스택 자료구조를 활용 , 구현 시에는 재귀함수로 구현.

"""


def dfs(data,visited,now):
    visited[now]=True
    print(now,end=" ")
    for i in data[now]:
        if not visited[i]:
            dfs(data,visited,i)

graph=[[0],[2,3,8],[1,7],[4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited=[False]*9

dfs(graph,visited,1)
