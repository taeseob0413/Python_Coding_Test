"""
도시 분할 문제

마을에 N개의 집과 M개의 길이 존재 한다.
마을을 2개로 분할하고 각 마을에 존재하는 집에는 1개이상의 길만 남겨놓도록 한다.(마을에는 적어도 1개의 집이 필요함)
이때 각 길에는 유지비가 있으므로 유지비를 최소로 하고 마을을 두개로 분할하는 문제

M이 1~100만이므로 O(MlogM)인 크루스칼 알고리즘을 사용할 경우에 가능.
또한 유지비를 최소로 하면서 마을을 분할해야 하므로 크루스칼 알고리즘을 사용한 뒤 가장 마지막에 추가되는 길(가장 비용이 비싼 길)을 제거하면 되는 문제.
"""
import sys
input=sys.stdin.readline

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
for _ in range(e):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
edges.sort(key=lambda x:x[0])
result=0
last=0
for edge in edges:
    a,b,c=edge
    if find_parent(parent,b)!=find_parent(parent,c):
        union_parent(parent,b,c)
        result+=a
        last=a
print(result-last)