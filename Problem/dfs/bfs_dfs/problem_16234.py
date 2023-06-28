"""
인구 이동 문제

NxN의 땅이 주어질 때 r행c열에 살고있는 인구가 주어진다.
이때 각각의 땅에서는 인접한 땅과의 인구 차이가 L~R사이이면 동맹을 맺고 국경을 열어서 인구이동을 한다.
동맹땅의 각 인구는 총인구//연합을 이루는 칸의 개수 이다.

몇 번의 인구이동이 발생하는지 구하기.

우선 시간복잡도를 고려할 때 인구이동이 2000번 이하로 발생한다는 조건이 있으므로 BFS 또는 DFS를 사용할 경우에 O(2500*2000)으로 볼 수 있다.
"""
from collections import deque

n,l,r=map(int,input().split())
#인구수 입력받기
graph=list()
for _ in range(n):
    graph.append(list(map(int,input().split())))

move_x=[1,-1,0,0]
move_y=[0,0,-1,1]

def bfs(start_x,start_y,graph,l,r,visit):

    visit[start_x][start_y]=True
    q=deque()
    q.append((start_x,start_y))
    result=[]
    result.append((start_x,start_y))
    sum=graph[start_x][start_y]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+move_x[i]
            ny=y+move_y[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph):
                if l<=abs(graph[x][y]-graph[nx][ny])<=r and visit[nx][ny]==False:
                    visit[nx][ny]=True
                    q.append((nx,ny))
                    result.append((nx,ny))
                    sum+=graph[nx][ny]
    if len(result)<=1:
        return False
    else:
        return (result,sum)
count=0
while True:
    result_list=list()
    visit=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            re=bfs(i,j,graph,l,r,visit)
            if re==False:
                continue
            else:
                result_list.append(re)
    if len(result_list)<=0:
        break
    else:
        count+=1
        for ingu in result_list:
            for x in ingu[0]:
                graph[x[0]][x[1]]=int(ingu[1]/len(ingu[0]))
print(count)