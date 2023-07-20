"""
감시 피하기 문제
"""
from itertools import combinations
import copy
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(str,input().split())))

#벽을 설치할 수 있는 공간을 모으는 리스트
target=[]
teachers=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='X':
            target.append((i,j))
        if graph[i][j]=='T':
            teachers.append((i,j))
targets=list(combinations(target,3))



def dfs(start, tmp,direction):
    x, y = start
    if x<0 or x>=len(tmp) or y<0 or y>=len(tmp):
        return True
    if tmp[x][y]=="S":
        return False
    if tmp[x][y]=="O":
        return True

    if direction==0:
        return dfs((x+1,y),tmp,direction)
    elif direction==1:
        return dfs((x-1,y),tmp,direction)
    elif direction==2:
        return dfs((x,y+1),tmp,direction)
    else:
        return dfs((x,y-1),tmp,direction)
flag=True
for t1,t2,t3 in targets:
    flag=True

    tmp=copy.deepcopy(graph)
    tmp[t1[0]][t1[1]]='O'
    tmp[t2[0]][t2[1]]='O'
    tmp[t3[0]][t3[1]]='O'

    for teacher in teachers:
        t1=dfs(teacher,tmp,0)
        t2 = dfs(teacher, tmp, 1)
        t3 = dfs(teacher, tmp, 2)
        t4 = dfs(teacher, tmp, 3)

        if not (t1 and t2 and t3 and t4):
            flag=False
            break
    if flag:
        print("YES")
        break
if flag==False:
    print("NO")

