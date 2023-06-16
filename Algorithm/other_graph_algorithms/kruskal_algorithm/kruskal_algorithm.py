"""
신장 트리 : 신장트리란 그래프가 주어졌을 때 모든 노드를 연결하고 사이클이 발생하지 않도록 하는 그래프의 부분 그래프이다.

최소 신장 트리 : 최소한의 비용을 갖는 신장트리를 의미함.
최소 신장 트리를 찾는 알고리즘으로는 크루스칼 알고리즘이 존재한다. (그리디)
1. 간선을 비용을 기준으로 오름차순 정렬 2. union연산시 사이클이 발생하는지 판별해서 사이클이 발생하지 않을 경우에만 연결 3. 2번과정을 반복함.
"""
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)
for i in range(1,v+1):
    parent[i]=i

edges=[]
result=0
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
edges.sort()

for edge in edges:
    if find_parent(parent,edge[1])!=find_parent(parent,edge[2]):
        union_parent(parent,edge[1],edge[2])
        result+=edge[0]

print(result)