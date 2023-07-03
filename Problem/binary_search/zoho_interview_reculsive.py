"""
어떤 원소의 첫번째 인덱스와 마지막 인덱스를 찾는 함수를 구현하기
"""
def binary_start(start,end,target,array):
    global min_index
    if start>end:
        return None
    mid=(start+end)//2

    if array[mid]==target:
        min_index=mid
        return binary_start(start,mid-1,target,array)
    elif array[mid]>target:
        return binary_start(start, mid - 1, target, array)
    else:
        return binary_start(mid+1, end, target, array)


def binary_last(start, end, target, array):
    global max_index
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        max_index = mid
        return binary_last(mid + 1, end, target, array)
    elif array[mid]>target:
        return binary_last(start, mid - 1, target, array)
    else:
        return binary_last(mid + 1, end, target, array)
min_index=0
max_index=0

n,x=map(int,input().split())
num_list=list(map(int,input().split()))

binary_start(0,len(num_list)-1,x,num_list)
binary_last(0,len(num_list)-1,x,num_list)
print(max_index,min_index)
print(max_index-min_index)