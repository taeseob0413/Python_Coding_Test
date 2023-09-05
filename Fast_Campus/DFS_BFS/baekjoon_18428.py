"""
감시 피하기 문제

N이 주어질 때 (N은 6이하) NXN의 지도가 주어지고 학생,선생님,빈칸이 각각 S,T,X로 주어질 떄 3개의 장애물을 설치하여 모든 학생이
선생님의 감시로부터 피할 수 있을 경우 "YES",못 피할경우 "NO"를 출력하는 문제

>>이 문제의 경우에는 예전 바이러스, 벽돌문제와 같음 / N이 6이하이므로 시간 복잡도는 크게 고려하지 않아도 되는 문제
>>dfs로 풀어보기
"""
from itertools import combinations
import sys
import copy

input=sys.stdin.readline

n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(str,input().split())))

#장애물을 설치하기 위한 빈칸.
vacant=[]
teachers=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='X':
            vacant.append((i,j))
        if graph[i][j]=='T':
            teachers.append((i,j))
#[[(1,1),(2,2),(3,3)],[(1,2),(2,2),(3,3)]....]
bbb=list(combinations(vacant,3))

move_x=[1,-1,0,0]
move_y=[0,0,1,-1]

def dfs(x,y,data):
    for i in range(x+1,len(data)):
        if data[i][y]=="S":
            return False
        elif data[i][y]=="O":
            break
    for i in range(x,-1,-1):
        if data[i][y]=="S":
            return False
        elif data[i][y]=="O":
            break
    for i in range(y+1,len(data)):
        if data[x][i]=="S":
            return False
        elif data[x][i]=="O":
            break
    for i in range(y,-1,-1):
        if data[x][i]=="S":
            return False
        elif data[x][i]=="O":
            break

    return True

#모든 경우에 대해 조사
flag=False
for t1,t2,t3 in bbb:
    tmp=copy.deepcopy(graph)
    tmp[t1[0]][t1[1]],tmp[t2[0]][t2[1]],tmp[t3[0]][t3[1]]='O','O','O'
    flag=True
    for a,b in teachers:
        if dfs(a,b,tmp)==False:
            flag=False
            break

    if flag:
        print("YES")
        break
if flag==False:
    print("NO")

