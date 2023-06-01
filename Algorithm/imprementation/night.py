"""
왕실의 나이트 문제
체스판에서 나이트는 L자로 울짐일 수 있음.
행 위치는 1~8로 표현 / 열 위치는 a~h로 표현
위치가 주어졌을 때 나이트가 움직일 수 있는 방법의 수 구하기

이 문제는 앞의 상하좌우와 같이 시뮬레이션 문제라고 볼 수 있음.
나이트가 움직일 수 있는 방법은 총 8가지가 존재하고 주어진 범위 내에 있도록 하는 것을 마지막으로 확인 하면 됨.
"""
move_x=[2,2,-2,-2,1,-1,1,-1]
move_y=[1,-1,1,-1,2,2,-2,-2]

curxy=input()
count=0
for i in range(8):   #움직일 수 있는 경우는 총 8가지
    nx,ny=0,0
    nx=ord(curxy[0])+move_x[i]
    ny=int(curxy[1])+move_y[i]
    if ord("a")<=nx<=ord("h") and 1<=ny<=8:
        count+=1
print(count)