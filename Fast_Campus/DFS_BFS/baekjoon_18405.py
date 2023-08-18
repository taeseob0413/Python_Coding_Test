"""
백준 18405 - 경쟁적 전염 문제

N,K가 주어지고 NXN의 지도가 주어진다.
이때 빈칸은 0 바이러스가 있는 칸은 1~K의 번호로 주어진다.
매초마다 바이러스는 오름차순으로 증식을 하는데 상,하,좌,우로 번식을 한다.
이때 S초 뒤에 X,Y에 존재하는 바이러스의 번호를 출력하는 문제.

>>이 문제는 N이 200이하이고 S가 10000 이하이므로 O(SN)의 시간 복잡도로 풀 수 있다.
>>또한 오름차순으로 바이러스를 증식시켜야 하므로 BFS를 이용하면 된다.
"""
import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

s,x,y=map(int,input().split())

#초기 바이러스의 위치들을 파악하는 과정
virus=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            #바이러스 번호(정렬을 위해 맨 앞에 위치),바이러스 위치, 처음 시간은 0
            virus.append((graph[i][j],(i,j),0))

#바이러스의 번호로 오름차순 실행
virus.sort(key=lambda x:x[0])

q=deque()

for i in range(len(virus)):
    q.append(virus[i])

move_x=[-1,1,0,0]
move_y=[0,0,-1,1]

while q:
    vir,location,time=q.popleft()
    if time>=s:
        break
    for i in range(4):
        nx,ny=location[0]+move_x[i],location[1]+move_y[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=vir
                q.append((vir,(nx,ny),time+1))

print(graph[x-1][y-1])