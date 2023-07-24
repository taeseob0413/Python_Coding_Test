"""
나무 자르기

O(NlogM) = 1*10^6 * log 2*10^9 =10^6 * log 2^31 = 31*10^6 = 3100만번의 연산
"""
import sys
input=sys.stdin.readline

n,target=map(int,input().split())
num_list=list(map(int,input().split()))

max_length=0

def binary_max(start,end,target):
    global max_length
    while start<=end:
        sum=0
        mid=(start+end)//2
        for i in num_list:
            if mid<=i:
                sum+=i-mid

        if sum>=target:
            start=mid+1
            max_length=mid
        else:
            end=mid-1

binary_max(1,max(num_list),target)
print(max_length)