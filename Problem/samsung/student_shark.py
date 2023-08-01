"""
청소년 상어 문제
"""
#물고기의 움직임 1~8
move_x=[-1,-1,0,1,1,1,0,-1]
move_y=[0,-1,-1,-1,0,1,1,1]

#방향 이동 함수
def turn_function(location,graph):
    count=0
    x,y=location
    direction=graph[x][y][1]
    print(direction)
    while True:
        count+=1
        nx, ny = x + move_x[direction], y + move_y[direction]
        print(x,y,move_x[direction],move_y[direction])
        print(nx,ny)
        if 0 <= nx < 4 and 0 <= ny < 4:
            if graph[nx][ny][0] != -1:
                return direction
        if direction==7:
            direction=0
        else:
            direction+=1

        if count==8:
            return False

result=0
x,y=0,0
graph=[[] for _ in range(4)]

for k in range(4):
    sub_list=list(map(int,input().split()))
    for i in range(4):
        a,b=sub_list[2*i],sub_list[2*i+1]
        graph[k].append([a,b-1])

#초기 상어의 좌표 설정
result+=graph[x][y][0]
graph[x][y][0]=-1
print(graph)
for i in range(16):
    dx,dy=-1,-1
    for a in range(4):
        for b in range(4):
            if graph[a][b][0]==i+1:
                dx,dy=a,b
    print((dx,dy),graph[dx][dy][-1])
    d=turn_function((dx,dy),graph)

    if d == False:
        continue
    else:
        graph[dx][dy][-1] = d
        graph[dx][dy], graph[dx + move_x[d]][dy + move_y[d]] = graph[dx + move_x[d]][dy + move_y[d]], graph[dx][dy]
    print(graph)
    print("")
print(graph)