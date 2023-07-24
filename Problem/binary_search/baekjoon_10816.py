"""
숫자 카드 2 문제

1. bisect라이브러리 사용
2. 함수 구현
"""
from bisect import bisect_left,bisect_right
import sys

input=sys.stdin.readline

n=int(input())
num_list=list(map(int,input().split()))
m=int(input())
targets=list(map(int,input().split()))

num_list.sort()

for i in targets:
    if bisect_left(num_list,i)==-1:
        print(0,end=' ')
    else:
        print(bisect_right(num_list,i)-bisect_left(num_list,i),end=' ')