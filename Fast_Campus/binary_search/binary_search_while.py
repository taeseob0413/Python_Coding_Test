"""
이진탐색 - 반복문으로 구현
"""

def binary_search_while(data,start,end,target):

    while start<=end:
        mid=(start+end)//2
        if data[mid]==target:
            return mid
        elif data[mid]>target:
            end=mid-1
        else:
            start=mid+1

    return False

num_list=[1,2,3,4,5,6,7,8,9]
result=binary_search_while(num_list,0,len(num_list)-1,5)

if result:
    print(result)
else:
    print("X")