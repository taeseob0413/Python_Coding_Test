"""
연구소 문제 2회독

>>이 문제는 N,M 8 이하의 아주 작은 수라는 점에서 시간은 크게 고려하지 않아도 된다는 점에 있음.
>>우선 모든 경우를 고려하여야 하기 때문에 combination을 사용하여 벽, 바이러스가 없는 빈 공간 중에서 3개를 뽑아서
>>모든 경우에 대해 bfs를 진행할 예정임.
"""
import copy
from collections import deque
from itertools import combinations

n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

vacant=[]

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            vacant.append((i,j))

targets=list(combinations(vacant,3))
max_safety=-1
move_x=[1,-1,0,0]
move_y=[0,0,1,-1]
def bfs (tmp,start):
    q=deque()
    q.append(start)

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+move_x[i]
            ny=y+move_y[i]
            if 0<=nx<len(tmp) and 0<=ny<len(tmp[0]):
                if tmp[nx][ny]==0:
                    tmp[nx][ny]=2
                    q.append((nx,ny))

for t1,t2,t3 in targets:
    count=0
    tmp=copy.deepcopy(graph)
    tmp[t1[0]][t1[1]]=1
    tmp[t2[0]][t2[1]]=1
    tmp[t3[0]][t3[1]]=1

    for i in range(n):
        for j in range(m):
            if graph[i][j]==2:
                bfs(tmp,(i,j))

    for a in range(n):
        for b in range(m):
            if tmp[a][b]==0:
                count+=1
    max_safety=max(max_safety,count)
print(max_safety)