"""
게임 개발 문제의 답 소스코드

해답코드에서는 따로 테두리 처리를 하지 않았고 처음제공 되는 map이외에 방문을 처리하는 리스트를 구현하였음.
>>문제를 풀 때 조건 중에서 외각은 전부 바다로 둘러쌓여 있다는 조건이 있었음.. 테두리 고려 안해도 되는 문제였음.
"""

n,m=map(int,input().split())

#방문처리를 위한 리스트
d=[[0]*m for _ in range(n)]

x,y,direction=map(int,input().split())
#현재의 위치를 입력받고 방문 처리
d[x][y]=1

#게임의 지도 입력 받기
game_map=[]
for _ in range(n):
    game_map.append(list(map(int,input().split())))

#북,동,남,서 방향 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]


#다음으로 회전하는 함수 구현
def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

count=1 #첫번째 지역은 방문했으므로 count 처리
turn_time=0 #네번 돌았는지 확인

while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    if d[nx][ny]==0 and game_map[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        if game_map[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_time=0
print(count)