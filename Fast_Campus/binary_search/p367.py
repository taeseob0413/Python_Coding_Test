"""
정렬된 배열에서 특정 수의 개수 구하기 문제

N개의 원소가 존재할 때 특정 원소가 주어질 때 특정 원소의 갯수를 출력하는 문제
O(logN)의 시간복잡도로 풀어야 한다.

>>만약 O(N)의 시간복잡도로 구할 수 있다면 계수정렬로도 가능하겠지만 O(logN)의 시간복잡도로 구하여야 하므로 이진 탐색을 사용하여야 한다.
>>두 가지 풀이가 존재
>>1. 이진 탐색을 직접 구현하는 경우
>>2. bisect 라이브러리 사용
"""
from bisect import bisect_left,bisect_right

n,k=map(int,input().split())
num_list=list(map(int,input().split()))

#1 bisect라이브러리 사용
result_bisect=bisect_right(num_list,k)-bisect_left(num_list,k)

#만약 값이 존재하지 않을 경우에는 bisect_right,bisect_left가 같은 값을 반환하여 result=0이 됨
if result_bisect==0:
    print(-1)
else:
    print(result_bisect)


#2 이진탐색 직접 구현

#가장 처음 인덱스와 가장 끝 인덱스를 담을 변수
first_index=-1
last_index=-1

def binary_first(data,start,end,target):

    global first_index

    while start<=end:
        mid=(start+end)//2

        if data[mid]>=target:
            end=mid-1
            first_index=mid
        else:
            start=mid+1

def binary_last(data,start,end,target):

    global last_index

    while start<=end:
        mid=(start+end)//2
        if data[mid]<=target:
            start=mid+1
            last_index=mid
        else:
            end=mid-1

binary_first(num_list,0,n-1,k)
binary_last(num_list,0,n-1,k)

if first_index==-1 or last_index==-1:
    print(-1)
else:
    print(last_index-first_index+1)
