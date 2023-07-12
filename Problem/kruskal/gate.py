"""
탑승구 문제

탑승구의 수 G와 비행기의 수 P가 주어지고 G,P<=십만
밑 줄부터는 i번째 비행기가 도킹할 수 있는 게이트의 범위가 주어질 때 최대한 많은 게이트에 비행기를 도킹하도록 하는 문제.

>>이 문제의 경우에는 각 도착하는 비행기마다 자신이 도킹할 수 있는 최대 탑승구의 번호에 도킹을 하면된다.
>>for문 두번을 이용하면 구할 수 있지만 O(GP)라는 점에서 시간초과가 발생할 것이다.
>>이때 서로로 자료구조를 사용하면 쉽게 구할 수 있다.
>>우선 0~G의 탑승구를 만들어 놓는다.
>>이후 도킹한 탑승구는 자신의 바로 왼쪽 탑승구와 union을 수행한다.
>>이렇게 계속 도킹을 하였을 때 만약 모든 탑승구의 루트가 0일 경우에 더이상 도킹을 할 수 없도록 구현하면 된다.
"""
def find_parent(parnet,x):
    if parnet[x]!=x:
        parnet[x]=find_parent(parnet,parnet[x])
    return parnet[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n=int(input())
m=int(input())
parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

result=0
ppp=[]
for _ in range(m):
    ppp.append(int(input()))
for data in ppp:
    if find_parent(parent,data)==0:
        break
    data=find_parent(parent,data)
    union_parent(parent,data,data-1)
    result+=1
print(result)