"""
서로소 자료구조 경로 압축

O(MV) >> O(V+M(1+logV))로 압축 가능
"""
#find 함수만 변경
def find_parent(parent,x):
    if parent[x] !=x:
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

for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

#각 원소가 속한 집단(각 원소의 루트 노드)
print("각 원소가 속한 집단 : ",end=" ")
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()

print("각 원소의 부모 노드",end=" ")
for i in range(1,v+1):
    print(parent[i],end=" ")
