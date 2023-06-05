"""
음료수 얼려 먹기
NxM의 얼음틀이 존재.
구멍이 뚫려 있는 부분은 0 칸막이가 존재하는 부분은 1로 주어진다.
이때 생성되는 총 아이스크림의 개수를 세기!!
bfs를 이용해서 문제를 푼 경우
"""
from collections import deque
n,m=map(int,input().split())
ice_map=[]
count=0
move_x=[1,-1,0,0]
move_y=[0,0,1,-1]

def bfs(start_x,start_y,graph):
    global count
    count+=1
    queue=deque([[start_x,start_y]])
    while queue:
        v=queue.popleft()
        for i in range(4):
            nx,ny=v[0]+move_x[i],v[1]+move_y[i]
            if 0<=nx<=n-1 and 0<=ny<=m-1:
                if graph[nx][ny]==0:
                    queue.append((nx,ny))
                    graph[nx][ny]=1

for _ in range(n):
    ice_sub=list(map(int,input()))
    ice_map.append(ice_sub)


for i in range(n):
    for j in range(m):
        if ice_map[i][j]==0:
            bfs(i,j,ice_map)

print(count)