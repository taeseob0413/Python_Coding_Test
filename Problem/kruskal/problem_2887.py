"""
행성 터널 문제
N개의 행성이 주어질 때 N-1개의 터널을 만들어서 모든 행성이 연결되도록 하는 문제.
단 두 행성간의 터널을 연결할 때 드는 비용은 min((x1-x2),(y1-y2),(z1-z2))이다.
이때 비용이 최소가 되도록 N-1개의 터널을 연결

>>이 문제는 크루스칼 알고리즘으로 풀 수 있다.
>>다만 만약 모든 간선을 고려한다면 N*(N-1)/2개의 간선이 고려되므로 O(ElogE)의 시간복잡도를 갖더라도 시간초과가 발생한다.
>>즉 간선의 갯수를 줄이는 작업이 필요하다.
>>이때 x축,y축,z축 각각 3개의 축으로 정렬을 한 간선의 개수 3(N-1)개만 고려하면 알맞은 시간 복잡도 내에 풀 수 있다.
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
x=[]
y=[]
z=[]
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

for i in range(1,n+1):
    a,b,c=map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()
edges=[]
result=0
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0],x[i+1][1],x[i][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i + 1][1], y[i][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i + 1][1], z[i][1]))
edges.sort()

for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(result)