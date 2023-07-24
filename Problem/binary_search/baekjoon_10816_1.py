"""
10816문제 bisect라이브러리 사용없이 구현하기
"""
import sys

input=sys.stdin.readline

n=int(input())
num_list=list(map(int,input().split()))
m=int(input())
targets=list(map(int,input().split()))

num_list.sort()

min_index=-1
max_index=-1


def binary_first(start, end, target, array):
    global min_index
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= target:
            end = mid - 1
            min_index = mid
        else:
            start = mid + 1


def binary_last(start, end, target, array):
    global max_index
    while start <= end:
        mid = (start + end) // 2
        if array[mid] <= target:
            start = mid + 1
            max_index = mid
        else:
            end = mid - 1


for i in targets:
    min_index=-1
    max_index=-1
    binary_first(0,n-1,i,num_list)
    binary_last(0, n - 1, i, num_list)
    if max_index==-1 or min_index==-1:
        print(0,end=' ')
    else:
        print(max_index-min_index+1,end=' ')
