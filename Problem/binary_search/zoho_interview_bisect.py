"""
조호 인터뷰 문제
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있음.
이때 수열에서 x가 등장하는 갯수를 구하시오.
"""
from bisect import bisect_left,bisect_right
n,x=map(int,input().split())
num_list=list(map(int,input().split()))

a=bisect_right(num_list,x)-bisect_left(num_list,x)
if a==0:
    print(-1)
else:
    print(a)