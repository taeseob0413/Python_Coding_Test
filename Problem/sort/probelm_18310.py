"""
안테나 문제
"""

n=int(input())
num_list=list(map(int,input().split()))
num_list.sort()

if n%2==0:
    print(num_list[n//2-1])
else:
    print(num_list[n//2])
