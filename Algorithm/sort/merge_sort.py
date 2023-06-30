"""
병합 정렬
분할 정복 알고리즘을 사용하는 정렬 알고리즘
리스트를 절반으로 자르는 작업을 계속하여 마지막으로 리스트를 나눈 뒤 재귀적으로 병합 정렬을 이용하여 병합한다.
O(NlogN)의 시간복잡도를 갖음.
"""
import random
def merge(left,right):
    lp,rp=0,0
    merge_list=list()

    #병합하는 left,right 리스트에 모두 원소가 있을 경우
    while lp<len(left) and rp<len(right):
        if left[lp]<right[rp]:
            merge_list.append(left[lp])
            lp+=1
        else:
            merge_list.append(right[rp])
            rp+=1

    #left리스트에 원소만 존재하는 경우
    while lp<len(left):
        merge_list.append(left[lp])
        lp+=1
    #right리스트에 원소만 존재하는 경우
    while rp<len(right):
        merge_list.append(right[rp])
        rp+=1
    return merge_list

def merge_split(data):
    if len(data)<=1:
        return data
    mid=int(len(data)/2)
    #left=merge_split(data[:mid])
    #right=merge_split(data[mid:])
    left=data[:mid]
    right=data[mid:]
    return merge(merge_split(left),merge_split(right))

num_list=random.sample(range(100),50)
num_list=merge_split(num_list)
print(num_list)