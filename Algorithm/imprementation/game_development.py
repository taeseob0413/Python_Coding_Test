"""
게임 개발 문제

"""

n,m=map(int,input().split())
x,y,stat=map(int,input().split())
x+=1
y+=1
game_map=list()
count=1


game_map.append([-1]*(m+2))
for i in range(n):
    sub_map=list(map(int,input().split()))
    game_map.append([-1]+sub_map+[-1])
game_map.append([-1]*(m+2))

#이동을 할 수 없는 방향 : 바다(1) , 테두리(-1) , 가봤던 칸(2) >> 테두리를 설정할 경우 벗어나서 이동하는 것을 걱정할 필요 없음
not_move=[-1,1,2]
game_map[x][y]=2
while True:
    if game_map[x-1][y] in not_move and game_map[x+1][y] in not_move and game_map[x][y+1] in not_move and game_map[x][y-1] in not_move:
        if (stat ==0 and game_map[x+1][y] in [-1,1]) or (stat == 3 and game_map[x][y+1] in [-1,1]) or (stat ==2 and game_map[x-1][y] in [-1,1]) or (stat==1 and game_map[x][y-1] in [-1,1]):
            break
        else:
            if stat==0 :  x+=1
            elif stat==1 : y-=1
            elif stat==2 : x-=1
            elif stat==3 : y+=1
    else:
        if stat==0:
            if game_map[x-1][y] in not_move:
                stat=3
            else:
                x-=1
                game_map[x][y]=2
                count+=1
        elif stat == 1:
            if game_map[x][y+1] in not_move:
                stat=0
            else:
                y+=1
                game_map[x][y] = 2
                count += 1
        elif stat == 2:
            if game_map[x+1][y] in not_move:
                stat=1
            else:
                x+=1
                game_map[x][y] = 2
                count+=1
        elif stat == 3:
            if game_map[x][y-1] in not_move:
                stat=2
            else:
                y-=1
                game_map[x][y] = 2
                count += 1

print(count)






