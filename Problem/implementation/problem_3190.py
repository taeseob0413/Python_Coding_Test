"""
뱀 문제

"""
#맵 초기화 >> 사과가 있는 곳은 a로표시 없는 곳은 0으로 표시
n=int(input())
graph=[[0]*(n) for _ in range(n)]

m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]='a'

k=int(input())
step=[]
for _ in range(k):
    a,b=map(str,input().split())
    step.append((a,b))

#머리와 꼬리의 초기좌표
head=[0,0]
tail=[0,0]

#동,남,서,북 >>시계방향으로 초기화
move_x=[0,1,0,-1]
move_y=[1,0,-1,0]

#초기 방향은 동쪽
direction=0

#시간 초기화
count=0

#초기 뱀이 존재하는 구간
graph[0][0]=1

while True:
    count += 1
    x,y=head[0],head[1]


    nx=x+move_x[direction]
    ny=y+move_y[direction]

    #한 칸 옮겼을 때 벽일 경우
    if nx<0 or nx>=n or ny<0 or ny>=n:
        break

    else:
        #자신의 몸과 마주칠 경우
        if graph[nx][ny]!=0 and graph[nx][ny]!='a':
            break
        #사과와 마주칠 경우
        elif graph[nx][ny]=='a':

            graph[nx][ny]=graph[head[0]][head[1]]+1
            head[0],head[1]=nx,ny
        elif graph[nx][ny]==0:

            graph[nx][ny]=graph[head[0]][head[1]]+1
            head[0], head[1] = nx, ny

            for i in range(4):
                nnx,nny=tail[0]+move_x[i],tail[1]+move_y[i]
                if 0<=nnx<n and 0<=nny<n:
                    if graph[nnx][nny]==graph[tail[0]][tail[1]]+1:
                        graph[tail[0]][tail[1]]=0
                        tail[0],tail[1]=nnx,nny
    # 방향을 바꾸는 구간이 존재할 때
    for i in range(len(step)):
        if count == int(step[i][0]):
            if step[i][1] == "L":
                if direction == 0:
                    direction = 3
                else:
                    direction -= 1
            elif step[i][1] == "D":
                if direction == 3:
                    direction = 0
                else:
                    direction += 1

print(count)
