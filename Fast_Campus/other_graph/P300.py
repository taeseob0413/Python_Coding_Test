"""
도시 분할 계획 문제

N개의 집과 M개의 도로가 존재할 때 마을을 두개의 마을로 최소한의 비용으로 나누고 싶을 때 최소 비용을 구하는 문제

>>최소 신장트리를 구한다음 맨 마지막에 더해지는 도로를 제외하면 된다.
>>M이 100만이므로 O(MlogM)의 시간 복잡도 안에 끝낼수 있음.
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

n,m=map(int,input().split())
edges=[]
parent=[0]*(n+1)

for i in range(n+1):
    parent[i]=i

for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

edges.sort()
result=0
count=0

for edge in edges:
    cost,x,y=edge
    if find_parent(parent,x)!=find_parent(parent,y):
        if count==n-2:
            break
        else:
            count+=1
            result+=cost
            union_parent(parent,x,y)

print(result)
