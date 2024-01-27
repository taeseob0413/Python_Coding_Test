"""
트로미노

>>이 문제의 경우에는 아이디어를 생각하면 빠르게 풀 수 있는 문제
>>우선 긴 격자의 경우에는 1*3 / 3*1 의 두 가지 경우를 생각하고
>>ㄴ 자 모양의 경우에는 모든 경우에서의 합의 최대를 구하는 것이기 때문에
>>2*2격자에서 가장 작은 수를 뺀것을 확인해나가면 된다.
"""
n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))
max_num=0

def get_num_22(r,c):
    global max_num
    total=0
    for i in range(r,r+2):
        for j in range(c,c+2):
            total+=graph[i][j]
    total-=min(graph[r][c],graph[r+1][c],graph[r][c+1],graph[r+1][c+1])
    max_num=max(max_num,total)

def get_num_13(r,c):
    global max_num
    total=0

    for i in range(c,c+3):
        total+=graph[r][i]
    max_num=max(max_num,total)

def get_num_31(r,c):
    global max_num
    total=0
    for i in range(r,r+3):
        total+=graph[i][c]
    max_num=max(max_num,total)

for i in range(n):
    for j in range(m):
        if i+1<n and j+1<m:
            get_num_22(i,j)
        if j+2<m:
            get_num_13(i,j)
        if i+2<n:
            get_num_31(i,j)
print(max_num)