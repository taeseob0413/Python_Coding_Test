"""
랜선 자르기 문제
"""
import sys

input=sys.stdin.readline

k,n=map(int,input().split())
num_list=[]
for _ in range(k):
    num_list.append(int(input()))
num_list.sort()
max_length=0
def binary_max(start,end,target):
    global max_length
    while start<=end:
        count=0
        mid=(start+end)//2
        for i in num_list:
            count+=i//mid

        if count>=target:
            max_length=mid
            start=mid+1
        else:
            end=mid-1
binary_max(1,max(num_list),n)
print(max_length)

