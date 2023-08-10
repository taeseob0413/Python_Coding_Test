""""
이진 탐색 - 재귀로 구현
"""

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

num_list=[1,2,3,4,5,6,7,8,9]
result=binary_search_reculsive(num_list,0,len(num_list)-1,11)

if result:
    print(result)
else:
    print("X")