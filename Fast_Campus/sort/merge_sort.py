"""
퀵 정렬과 같이 분할과 정복 알고리즘을 사용하는 정렬 알고리즘
O(NlogN)의 시간 복잡도를 갖고 있음.
"""
import random

def merge_split(data):
    if len(data)<=1:
        return data

    mid=len(data)//2
    left=merge_split(data[:mid])
    right=merge_split(data[mid:])

    return merge(left,right)

def merge(left,right):
    lp,rp=0,0
    result=[]

    while lp<len(left) and rp<len(right):
        if left[lp]<right[rp]:
            result.append(left[lp])
            lp+=1
        else:
            result.append(right[rp])
            rp+=1
    while lp<len(left):
        result.append(left[lp])
        lp+=1
    while rp<len(right):
        result.append(right[rp])
        rp+=1
    return result

num_list=random.sample(range(100),50)
print(num_list)
num_list=merge_split(num_list)
print(num_list)