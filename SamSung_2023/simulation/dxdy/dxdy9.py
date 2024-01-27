"""
되돌아오기 문제 2
"""

#명령어 받기
ope=input()

#동서남북으로 dx,dy세팅하기
dx,dy=[0,1,0,-1],[1,0,-1,0]

#초기 방향, 좌표 세팅
dir=3
x,y=0,0

count=0

flag=False
for o in ope:
    count+=1
    #반시계 방향 회전
    if o=='L':
        dir=(dir+3)%4
    elif o=='R':
        dir=(dir+1)%4
    else:
        x,y=x+dx[dir],y+dy[dir]
        if x==0 and y==0:
            flag=True
            break

if flag:
    print(count)
else:
    print(-1)