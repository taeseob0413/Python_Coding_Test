"""
이진 탐색이란 순차 탐색과는 다르게 내부의 데이터가 정렬되어 있을 때 빠르게 원하는 값을 탐색할 수 있는 알고리즘이다.
이진 탐색은 시작점,끝점,중간점을 활용하여 원하는 데이터를 찾는다.
또한 한번의 탐색이 끝난 뒤 탐색의 범위를 절반으로 줄이기 때문에 O(logN)의 시간 복잡도를 갖는다.

>>이진 탐색 문제는 데이터의 개수가 많거나 탐색 범위가 매우 크다.
ex)데이터의 개수가 1000만개 이상이거나 탐색범위의 크기가 1,000억 이상일 경우 이진 탐색 알고리즘을 의심해보자!!
"""
#재귀적으로 구현
def binary_search_reculsive(start,end,target,array):
    #데이터가 존재하지 않는 경우
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search_reculsive(start,mid-1,target,array)
    else:
        return binary_search_reculsive(mid+1,end,target,array)


array=[1,3,5,7,9,11,15,17,19]
target=7

if binary_search_reculsive(0,len(array)-1,target,array)==None:
    print("원하는 데이터 X")
else:
    print("원하는 데이터는",binary_search_reculsive(0,len(array)-1,target,array),"에 존재")

#반복문으로 구현
def binary_search_iterable(start,end,target,array):
    while start<=end:
        mid = (start + end) // 2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None