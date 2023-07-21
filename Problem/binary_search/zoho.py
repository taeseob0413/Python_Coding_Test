"""
조호 인터뷰 문제

n개의 숫자가 주어질 때 x개의 숫자가 몇개 있는지 확인하는 문제 / 문제의 조건에서 O(logN)의 시간복잡도 요구

>>가장 쉽게 푸는 방법은 bisect라이브러리 사용
>>두번째는 이진탐색 코드 직접 짜기
"""
from bisect import bisect_left,bisect_right
n,x=map(int,input().split())
num_list=list(map(int,input().split()))

result=bisect_right(num_list,x)-bisect_left(num_list,x)
if result==0:
    print(-1)
else:
    print(result)

min_index=-1
max_index=-1

def binary_first(start,end,target,array):
    if start>end:
        return
    global min_index
    mid=(start+end)//2
    if array[mid]==target:
        min_index=mid
        return binary_first(start,mid-1,target,array)
    elif array[mid]>target:
        return binary_first(start,mid-1,target,array)
    else:
        return binary_first(mid+1,end,target,array)

def binary_last(start,end,target,array):
    if start>end:
        return
    global max_index
    mid=(start+end)//2
    if array[mid]==target:
        max_index=mid
        return binary_last(mid+1,end,target,array)
    elif array[mid]>target:
        return binary_first(start,mid-1,target,array)
    else:
        return binary_first(mid+1,end,target,array)

binary_first(0,n-1,x,num_list)
binary_last(0,n-1,x,num_list)
if max_index==-1:
    print(-1)
else:
    print(max_index-min_index+1)