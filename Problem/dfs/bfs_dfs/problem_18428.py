"""
감시 피하기 문제
"""

from itertools import combinations
import copy
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(str,input().split())))
brick=[]
teacher=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]=="X":
            brick.append((i,j))
        if graph[i][j]=="T":
            teacher.append((i,j))
check_brick=list(combinations(brick,3))

def dfs(start,tar,graph):
    if 0<=start[0]<len(graph) and 0<=start[1]<len(graph):
        if graph[start[0]][start[1]]=="S":
            return False
        if graph[start[0]][start[1]]=="O":
            return True
        if tar==1:
            return dfs((start[0]+1,start[1]),tar,graph)
        elif tar==2:
            return dfs((start[0]-1,start[1]),tar,graph)
        elif tar==3:
            return dfs((start[0],start[1]+1),tar,graph)
        elif tar==4:
            return dfs((start[0],start[1]-1),tar,graph)
    return True

flag = True
for check in check_brick:
    flag = True
    t1,t2,t3=check
    tmp=copy.deepcopy(graph)
    tmp[t1[0]][t1[1]]="O"
    tmp[t2[0]][t2[1]]="O"
    tmp[t3[0]][t3[1]]="O"
    for tea in teacher:
        o1,o2,o3,o4=dfs(tea,1,tmp),dfs(tea,2,tmp),dfs(tea,3,tmp),dfs(tea,4,tmp)
        if not o1 or not o2 or not o3 or not o4:
            flag=False
            break
    if flag==True:
        break


if flag:
    print("YES")
else:
    print("NO")