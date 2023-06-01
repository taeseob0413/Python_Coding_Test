"""
상하좌우 문제
NxN 지도에서 여행가는 (1,1)이라는 위치에서 시작을 하게 되고 주어진 이동계획에 따라 움직이게 된다.
이때 NxN 지도를 벗어날 수 없고 만약 벗어나게 되는 이동계획은 무시하게 됨.
이동계획을 전부 수행한 뒤 마지막으로 여행자가 서있는 위치를 반환하는 문제

이 문제의 경우에는 이동계획이 100개 이하이므로 시간복잡도에서 꽤나 자유로움.
문제의 포인트는 NxN을 벗어나지 않고 이동을 하는 것이므로 이동계획에 따라 이동을 한 뒤 NxN을 벗어났는지 확인한 후
아닐때에만 좌표를 변경하는 것이 중요
"""

n=int(input())
move_list=list(map(str,input().split()))
dx=[0,0,1,-1]
dy=[1,-1,0,0]  #각각 하상우좌를 뜻함.
cx=0
cy=0   #현재의 x,y좌표

for move in move_list:
    nx,ny=0,0  #이동을 했을 떄의 좌표
    if move=="R":
        nx=cx+dx[2]
        ny=cy+dy[2]
    elif move=="L":
        nx = cx + dx[3]
        ny = cy + dy[3]
    elif move=="U":
        nx = cx + dx[1]
        ny = cy + dy[1]
    elif move=="D":
        nx = cx + dx[0]
        ny = cy + dy[0]
    if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
    cx=nx
    cy=ny
print(cy+1, cx+1)


