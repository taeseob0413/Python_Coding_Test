"""
부품 찾기문제

N 종류의 전자제품이 존재하고 손님은 M 종류의 부품을 구매하고 싶어할 때 구매여부를 물어보는 문제
N<=백만, M<=십만

>>이 문제에서 순차탐색을 할 경우 시간복잡도가 O(MN) = 10^11이므로 시간초과 발생
>>이진 탐색을 사용하면 O(NlogN)의 정렬시간과 O(MlogN)의 탐색시간이 소요됨.
>>NlogN = 백만*log백만 이고 백만=2^20 이므로 약 2000만번의 수행으로 이 문제를 해결할 수 있어서 시간 복잡도에 위배되지 않는다.
>>정렬 알고리즘 연습을 위해서 퀵 정렬을 직접짜서 사용하기

cf)이 문제의 경우에는 계수 정렬을 사용하면 더 쉽게 풀 수 있음.
"""
import sys

def quick_sort(start,end,data):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end

    while left<=start:
        while left<=end and data[left]<=data[pivot]:
            left+=1
        while right>start and data[right]>=data[pivot]:
            right-=1
        if left>right:
            data[right],data[pivot]=data[pivot],data[right]
        else:
            data[left],data[right]=data[right],data[left]
    quick_sort(start,right-1,data)
    quick_sort(right+1,end,data)

def binary_search(start,end,target,array):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return True
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return False

input=sys.stdin.readline

n=int(input())
product=list(map(int,input().split()))
m=int(input())
cus=list(map(int,input().split()))

for i in cus:
    if binary_search(0,n-1,i,product):
        print("YES",end=' ')
    else:
        print("NO",end=' ')
