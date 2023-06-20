"""
기존에 풀었던 음료수 얼려먹기 문제
NXM의 얼음틀에 구멍이 뚫린 부분은 0 , 막혀있는 부분은 1로 주어진다.
한번에 만들 수 있는 아이스크림의 개수 출력문제

>>그래프 알고리즘으로 풀 수 있음.
>>dfs를 이용해서 풀어볼 예정.
"""

move_x=[-1,1,0,0]
move_y=[0,0,-1,1]
def dfs(start,graph):
    x,y=start
    graph[x][y]=1
    for i in range(4):
        nx=x+move_x[i]
        ny=y+move_y[i]
        if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
            if graph[nx][ny]==0:
                dfs((nx,ny),graph)

n,m=map(int,input().split())
graph=[]
count=0
for _ in range(n):
    graph_sub=list(map(int,input()))
    graph.append(graph_sub)
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            dfs((i,j),graph)
            count+=1

print(count)