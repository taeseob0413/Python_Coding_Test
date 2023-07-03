"""
아마존 인터뷰
고정점 찾기
고정점 : 수열에서 인덱스의 값과 그 수열의 값이 갖는 원소를 의마한다
오름차순으로 주어진 수열이 존재할 때 고정점이 존재할 경우에 고정점을 출력하기 / 고정점은 최대 1개만 존재한다.

>>이 문제에서 핵심은 mid==array[mid]값을 비교한뒤
array[mid]>mid 일 경우에는 인덱스가 mid보다 큰 쪽은 무조건 mid의 값보다 클 수 없다 따라서 작은 쪽으로 이진탐색을 진행하여 주는 것이 핵심이다.
"""

n=int(input())
num_list=list(map(int,input().split()))

def binary_search(start,end,array):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==mid:
            return mid
        elif array[mid]<mid:
            start=mid+1
        else:
            end=mid-1
    return None

if binary_search(0,len(num_list),num_list)==None:
    print(-1)
else:
    print(binary_search(0,len(num_list),num_list))