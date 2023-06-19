"""
팀 결성 문제

학생들은 0~N번까지의 번호를 부여받고 처음에는 각각 모두 다른 팀으로 N+1개의 팀이 존재한다.
이때 선생님은 M번의 연산을 할 수 있다.

만약 팀 합치기 연산을 할 경우에는 0 a b 형태로 연산이 주어지고
같은 팀 확인 연산을 후생할 경우에는 1 a b 의 연산의 형태로 주어진다.

1<=N,M<=100,000이므로 서로소 집합 자료구조를 사용하면 쉽게 풀 수 있음.
"""
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parnet(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)
for i in range(v+1):
    parent[i]=i

for _ in range(e):
    a,b,c=map(int,input().split())
    if a==0:
        union_parnet(parent,b,c)
    else:
        if find_parent(parent,b)==find_parent(parent,c):
            print("YES")
        else:
            print("NO")