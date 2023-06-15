"""
서로소 알고리즘 자료구조  >> union_find 자료구조라고도 한다.

그래프 알고리즘에서 중요하게 사용되는 자료구조로 트리를 사용하여 구현

union 연산 : 2개의 원소가 포함된 집단을 합치는 연산
find 연산 : 특정 원소가 속한 집단의 root 원소를 알려주는 연산

알고리즘 순서 : 1. union연산을 확인한 뒤 합치려는 A,B원소의 루트노드(C,D)를 찾는다. 2. 두 루트노드 C,D 중에서 작은 값을 C라 하면 D를 C에 연결한다.

구현할 때는 union과 find 두 함수를 구현한 뒤 부모테이블에 각 노드의 부모를 기록.  >> find 연산 O(V)
"""
#부모 노드를 찾는 find 함수
def find_parent(parent,x):
    #현재 x가 루트노드가 아닐 경우
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x

#두 원소가 속한 집단을 합치는 union함수
def union_parent(parent,a,b):
    #a,b의 루트 원소를 찾기
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

#처음에는 모두 자기자신이 root 노드
for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
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

"""
O(V)인 find 함수의 시간복잡도 개선을 위해 경로 압축을 사용할 수 있음.
"""
