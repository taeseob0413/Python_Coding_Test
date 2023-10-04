"""
크루스칼 알고리즘

크루스칼 알고리즘은 최소 신장트리를 찾을 때 사용하는 알고리즘 cf)신장트리 : 그래프에서 모든 노드를 포함하면서 사이클이 발생하지 않는 부분 그래프, v-1개의 간선
O(ElogE) : 크루스칼 알고리즘의 시간 복잡도 (모든 간선을 정렬하는데 드는 시간)
작동 원리
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 확인하면서 현재의 간선이 사이클을 발생시키는지 확인 >> 사이클이 없을 경우 Union / 사이클 있을 경우 Pass
"""
import sys

input=sys.stdin.readline

def find_parnet(parent,x):
    if parent[x]!=x:
        parent[x]=find_parnet(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parnet(parent,a)
    b=find_parnet(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
edges=[]
parent=[0]*(v+1)
result=0

for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

edges.sort()

for edge in edges:
    cost,a,b=edge
    if find_parnet(parent,a)!=find_parnet(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)