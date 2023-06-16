"""
사이클 판별하기 : 무방향 그래프에서의 사이클 판별은 서로소 자료구조를 활용하여 진행할 수 있다.
union연산 시 두 원소의 루트노드를 확인하여 같다면 사이클이 발생한 경우이고 아니면 사이클리 발생하지 않은 경우이다.
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
        parent[b]=a

v,e=map(int,input().split())
parent=[0]*(v+1)
cycle=False

for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생하지 않음.")