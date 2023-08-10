"""
부품 찾기 문제

가게에 N개의 제품이 존재할 때 손님은 M개의 부품이 필요하다.
손님이 필요한 M개의 제품 각각이 가게에 존재할 경우 yes, 없을 경우 no를 출력하는 문제

>>이 문제의 경우에는 순차탐색으로 풀 경우에 O(MN)의 시간 복잡도가 필요하며 N이 100만 M이 10만이므로 시간 초과가 발생하게 된다.
>>이때 가게의 물품을 오름차순으로 정렬한 뒤 이진탐색을 수행하게 되면 O(NlogN+MlogN)으로 알맞게 문제를 해결할 수 있다.
>>또한 계수정렬로도 풀 수 있음 계수 정렬로 풀 경웨 O(M+N)으로 가장 빠르게 문제를 해결할 수 있음.
"""
import sys

input=sys.stdin.readline

def quick_sort(data):
    if len(data)<=1:
        return data

    pivot=data[0]
    left=[item for item in data[1:] if item<=pivot]
    right=[item for item in data[1:] if item>pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)

def binary_search_reculsive(data,start,end,target):
    if start>end:
        return False

    mid=(start+end)//2
    if data[mid]==target:
        return mid
    elif data[mid]>target:
        return binary_search_reculsive(data,start,mid-1,target)
    else:
        return binary_search_reculsive(data,mid+1,end,target)



n=int(input())
store_list=list(map(int,input().split()))
store_list=quick_sort(store_list)


m=int(input())
purchase=list(map(int,input().split()))

for i in purchase:
    result=binary_search_reculsive(store_list,0,len(store_list)-1,i)

    if result==False:
        print("No",end=' ')
    else:
        print("Yes",end=' ')