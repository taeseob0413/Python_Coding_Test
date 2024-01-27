"""
격자에서의 dx,dy

한 점이 주어지고 상하좌우에 1이 몇개 존재하는지 카운트하는 경우

주의할 점

1. nx,ny가 각각 범위내에 들어오는지를 먼저 확인해야 한다 >> 함수로 구현해보자.
2. zip(리스트,리스트) 사용을 해도 됨.
"""
a = [[0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 0, 0, 1],
     [1, 0, 1, 1, 1],
     [1, 0, 1, 1, 0]]

x,y=2,4

dx,dy=[0,1,0,-1],[1,0,-1,0]

def in_range(a,b,n):
    return 0<=a<n and 0<=b<n

cnt=0

for c,d in zip(dx,dy):
    nx,ny=x+c,y+d

    if in_range(nx,ny,len(a)):
        if a[nx][ny]==1:
            cnt+=1

print(cnt)