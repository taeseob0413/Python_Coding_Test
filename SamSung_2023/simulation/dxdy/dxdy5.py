"""
작은 구슬의 이동
"""
#왼,오의 합과 위,아래의 합이 전부 3이 되도록 구현함 >> dir=3-dir로 구현할 수 있도록 함.
dx=[0,1,-1,0]
dy=[1,0,0,-1]

n,t=map(int,input().split())
mapper={
    'R':0,
    'D':1,
    'L':3,
    'U':2
}

a,b,c=map(str,input().split())

dir=mapper[c]
x,y=int(a)-1,int(b)-1

for i in range(t):
    nx,ny=x+dx[dir],y+dy[dir]
    if 0<=nx<n and 0<=ny<n:
        x,y=nx,ny
    else:
        dir=3-dir

print(x,y)