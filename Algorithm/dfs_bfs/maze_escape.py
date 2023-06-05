"""
미로 탈출 문제
첫 위치는 (1,1)로 고정되어 있고 괴물이 있는 부분은 0 괴물이 없는 부분이 1일 때
미로의 출구는 N,M에 존재한다.
이때 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하기!!

>>최단거리 문제임으로 BFS를 사용하기로 하였음.
"""
from collections import deque
n,m=map(int,input().split())
maze_map=[]
move_x=[1,-1,0,0]
move_y=[0,0,1,-1]
for _ in range(n):
    maze_sub=list(map(int,input()))
    maze_map.append(maze_sub)

def bfs(start_x,start_y):
    queue=deque()
    queue.append([start_x,start_y])
    while queue:
        v=queue.popleft()
        for i in range(4):
            nx=v[0]+move_x[i]
            ny=v[1]+move_y[i]
            if 0<=nx<=n-1 and 0<=ny<=m-1:
                if maze_map[nx][ny]==1:
                    maze_map[nx][ny]=maze_map[v[0]][v[1]]+1
                    queue.append([nx,ny])
bfs(0,0)
print(maze_map[n-1][m-1])
