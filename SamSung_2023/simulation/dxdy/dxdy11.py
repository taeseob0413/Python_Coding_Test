"""
거울 반사 문제
"""
n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(str,input())))

num=int(input())
num-=1
#방향, 시작 위치
#dir 0,1,2,3 >> 위쪽, 오른쪽, 밑, 왼쪽에서 접근 , start >> 시작 위치 1~0
dir,dd=num//n,num%n

start_x,start_y=0,0
#방향 0,1,2,3>>동남서북
direction=0

if dir==0:
    start_x,start_y=0,dd
    direction=1
elif dir==1:
    start_x,start_y=dd,n-1
    direction=2
elif dir==2:
    start_x,start_y=n-1,n-1-dd
    direction=3
else:
    start_x,start_y=n-1-dd,0
    direction=0

dx,dy=[0,1,0,-1],[1,0,-1,0]
result=0

while True:
    result+=1
    if graph[start_x][start_y]=='\\':
        if direction==1 or direction==3:
            direction=(direction+3)%4
        else:
            direction=(direction+1)%4
    else:
        if direction==1 or direction==3:
            direction=(direction+1)%4
        else:
            direction=(direction+3)%4
    start_x,start_y=start_x+dx[direction],start_y+dy[direction]
    if not (0<=start_x<n and 0<=start_y<n):
        break
print(result)
