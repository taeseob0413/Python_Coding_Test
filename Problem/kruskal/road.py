"""
어두운 길 문제

집의 갯수 N개와 도로의 갯수 M개가 주어진다.
이때 집과 집사이의 도로에 가로등이 존재하고 가로등을 하루동안 켜놓는 비용은 도로의 길이와 동일하다.
모든 집과 집사이의 도로에 가로등을 최소로 켰을 때 절약되는 비용을 구하는 문제

>>크루스칼 알로리즘을 이용하면 구할 수 있는 문제이다.
>>N,M이 20만이하이므로 O(ElogE)의 시간복잡도에서 구할 수 있다.
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

n,m=map(int,input().split())
edges=[]
parent=[0]*(n)
for i in range(n):
    parent[i]=i
total=0
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))
    total+=c

edges.sort()
result=0
for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(total-result)