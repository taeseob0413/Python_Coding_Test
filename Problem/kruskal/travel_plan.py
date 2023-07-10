"""
여행 계획 문제

N,M이 주어질 때 나라에는 N개의 여행지가 있다. (N,M<=500)

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
parent=[0]*(n+1)
for i in range(1,m+1):
    parent[i]=i

edges=[]
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

plan=list(map(int,input().split()))

for i in range(n):
    for j in range(i,n):
        if graph[i][j]==1:
            edges.append((i+1,j+1))


for edge in edges:
    a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
cycle=True
result=parent[plan[0]]
for i in range(1,len(plan)):
    if result!=parent[plan[i]]:
        cycle=False
        break

if cycle:
    print("YES")
else:
    print("NO")



