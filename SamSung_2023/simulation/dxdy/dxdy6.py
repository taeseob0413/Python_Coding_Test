"""
빙빙 돌며 숫자 적기

n * n크기의 정사각형에 숫자 1부터 순서대로 증가시키며
달팽이 모양으로 채우는 코드를 작성해보세요.

달팽이 모양이란 왼쪽 위 모서리에서 시작해서, 오른쪽, 아래쪽,
왼쪽, 위쪽 순서로 더 이상 채울 곳이 없을 때까지 회전하는 모양을 의미합니다.

>>벽을 마주했을 때 시계방향으로 도는게 포인트!!
"""

#시계방향으로 dx,dy설정
dx,dy=[0,-1,0,1],[1,-0,-1,0]

n=int(input())
graph=[[False]*(n) for _ in range(n)]
dir=0
x,y=0,0
count=0
graph[x][y]=1
while True:
    if count>=4:
        break
    nx,ny=x+dx[dir],y+dy[dir]
    #항상 좌표 설정 먼저해주기
    if 0<=nx<n and 0<=ny<n and graph[nx][ny]==False:
        graph[nx][ny]=graph[x][y]+1
        count=0
        x,y=nx,ny
    else:
        count+=1
        dir=(dir+1)%4

for i in range(n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print()