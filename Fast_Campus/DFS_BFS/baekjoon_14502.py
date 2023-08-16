"""
백준 14502 - 연구소 문제(삼성전자 sw 역량테스트)

첫째 줄에 N,M이 주어지고 (N,M 8이하)
그 뒤로 NxM의 지도가 주어진다.
지도에서 0은 빈칸, 1은 벽, 2는 바이러스가 있는 위치이다.
이때 벽을 3개 세워서 바이러스가 퍼질수 없는 공간의 최대 개수를 구하는 문제.

>>이 문제의 경우에는 N,M이 8이하 이므로 시간 복잡도는 크게 고려하지 않아도 된다.
>>또한 모든 빈칸 중에서 3개를 선택해야 하므로 itertools의 combinations 라이브러리를 사용하면 좋음
>>이때 고려해야할 모든 경우는 64컴비네이션 3 보다 작으므로 시간 복잡도를 만족시킨다.
"""
from itertools import combinations
from collections import deque
import sys
import copy

input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

#빈칸을 조사하는 과정
vacant=[]

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            vacant.append((i,j))

#빈 칸중에서 3개를 뽑는 경우를 전부 리스트로 반환
#bricks=[((0,0),(1,1),(2,2))......]
bricks=list(combinations(vacant,3))

move_x=[-1,1,0,0]
move_y=[0,0,-1,1]


def bfs(data,i,j):
    q=deque()
    q.append((i,j))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+move_x[i],y+move_y[i]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny]==0:
                    data[nx][ny]=2
                    q.append((nx,ny))
# 모든 가능한 경우의 수에 대해 조사
# bricks=((1,1),(2,2),(3,3))   >> t1=(1,1) t2=(2,2) ...
max_value = -1
for t1,t2,t3 in bricks:
    tmp=copy.deepcopy(graph)
    tmp[t1[0]][t1[1]],tmp[t2[0]][t2[1]],tmp[t3[0]][t3[1]]=1,1,1
    count=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                bfs(tmp,i,j)
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                count+=1

    if max_value<count:
        max_value=count


print(max_value)

