"""
K번째 수

>>N개의 오름차순 정렬을 수행했을 때 K번째의 수를 출력하는 문제
>>이 문제의 경우에는 데이터가 500만개이므로 시간 복잡도를 잘 고려해야하는 문제
>>O(NlogN)가능
"""
import sys

input=sys.stdin.readline

n,k=map(int,input().split())
num_list=list(map(int,input().split()))

def quick_sort(start,end,data):
    if start>end:
        return
    pivot=start
    left=start+1
    right=end

    while left<=right:
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

quick_sort(0,len(num_list)-1,num_list)
print(num_list[k-1])