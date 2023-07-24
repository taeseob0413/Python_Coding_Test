"""
수 찾기 문제
"""
import sys

input=sys.stdin.readline

n=int(input())
num_list=list(map(int,input().split()))
m=int(input())
targets=list(map(int,input().split()))

num_list.sort()

def binary_search(start,end,target,array):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            print(1)
            return
        elif array[mid]<target:
            start=mid+1
        else:
            end=mid-1
    print(0)
    return

for i in targets:
    binary_search(0,n-1,i,num_list)
