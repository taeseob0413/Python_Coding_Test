"""
되돌아오기 문제

N번의 명령어가 존재하고 명령어는 방향, 이동거리 순으로 주어짐
이때 몇초뒤에 원래의 자리로 돌아오는지 구하는 문제
만약 N개의 명령어가 끝난 뒤에도 돌아올 수 없다면 -1을 출력하는 문제

>>이 문제는 제한이 없으므로 나갔는지는 확인을 안해도 됨
"""

n=int(input())
mapper={
    'E':0,
    'S':1,
    'W':2,
    'N':3
}

x,y=0,0
dx,dy=[0,1,0,-1],[1,0,-1,0]
t=0
flag=False
for i in range(n):
    a,b=map(str,input().split())
    dir=mapper[a]

    for _ in range(int(b)):
        x,y=x+dx[dir],y+dy[dir]
        t+=1
        if x==0 and y==0:
            flag=True
            break

    if flag:
        break

if flag:
    print(t)
else:
    print(-1)


