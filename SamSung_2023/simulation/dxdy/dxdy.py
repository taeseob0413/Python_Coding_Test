"""
dx, dy 테크닉
>>이코테에서 시뮬레이션으로 공부를 했던 유형임.
"""

x,y=0,0
#동서남북 설정하기
dx=[0,0,-1,1]
dy=[1,-1,0,0]

#동서남북으로 움직인 좌표를 의미함
for i in range(4):
    nx,ny=x+dx[i],y+dy[i]

#dxdy문제 1번
n=int(input())

#동서남북을 의미
dx=[0,0,-1,1]
dy=[1,-1,0,0]

#동서남북
dir=["E","W","S","N"]

#초기 시작 (0,0)
x,y=0,0

for _ in range(n):
    a,b=map(str,input().split())
    w=int(b)
    for i in range(4):
        if a==dir[i]:
            x,y=x+dx[i]*w,y+dy[i]*w
            break
print(y,x)

