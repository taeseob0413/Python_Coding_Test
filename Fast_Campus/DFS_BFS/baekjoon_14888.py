"""
연산자 끼워넣기 문제

N개의 수가 주어지고 연산자는 사칙연산이 주어질 때 사용할 수 있는 연산자의 갯수를 고려하여 식을 만든다.
이때 계산은 무조건 왼쪽에서부터 시작을 한다. 단 나눗셈은 정수 나순셈으로 몫만 취하고 음수를 양수로 나눌 때는 음수를 양수로 만든뒤 계산한 결과에 -를 붙인다.
이떄 계산의 결과가 최대인 것과 최소인 것의 갯수를 구하는 문제 , 최댓값과 최솟값은 항상 -10억~10억사이

>>N이 11이하이므로 시간 복잡도는 크게 고려하지 않아도 된다.
"""
import sys
from collections import deque
input=sys.stdin.readline

#최댓값,최솟값 초기화
MAX_V=-int(1e9)
MIN_V=int(1e9)

n=int(input())
num_list=list(map(int,input().split()))


operations=list(map(int,input().split()))

def dfs(sum,data):
    global MAX_V
    global MIN_V

    if len(data)==0:
        if sum>MAX_V:
            MAX_V=sum
        if sum<MIN_V:
            MIN_V=sum
        return
    num=data[0]
    if operations[0]!=0:
        operations[0]-=1
        dfs(sum+num,data[1:])
        operations[0]+=1

    if operations[1]!=0:
        operations[1]-=1
        dfs(sum-num,data[1:])
        operations[1]+=1

    if operations[2]!=0:
        operations[2]-=1
        dfs(sum*num,data[1:])
        operations[2]+=1

    if operations[3]!=0:
        operations[3]-=1

        if sum<0:
            tmp=-((-sum)//num)
            dfs(tmp,data[1:])
        else:
            dfs(sum//num,data[1:])

        operations[3]+=1

sum=num_list[0]
dfs(sum,num_list[1:])
print(MAX_V)
print(MIN_V)