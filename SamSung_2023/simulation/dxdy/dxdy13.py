"""
빙빙 돌며 사각형 채우기

>>시계방향 회전 문제
>>단 알파벳을 채워가면서 Z일경우 다시 A로 돌아가서 채우는 문제
>>chr(숫자) : 아스키코드로 변환 / ord(문자) :  숫자로 변환
"""

n,m=map(int,input().split())
graph=[[0]*m for _ in range(n)]

dx,dy=[0,1,0,-1],[1,0,-1,0]
dir=0
x,y=0,0
graph[x][y]="A"
count=0
sss="B"
while True:
    nx,ny=x+dx[dir],y+dy[dir]
    if (0<=nx<n and 0<=ny<m) and graph[nx][ny]==0:
        graph[nx][ny]=sss
        if sss=="Z":
            sss="A"
        else:
            sss=chr(ord(sss)+1)
        x,y=nx,ny
        count=0
    else:
        dir=(dir+1)%4
        count+=1
    if count>=4:
        break

for i in range(n):
    for j in range(m):
        print(graph[i][j],end=" ")
    print()