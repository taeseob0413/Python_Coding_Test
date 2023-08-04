"""
퀵 정렬_리스트 comprehension 사용

퀵 정렬은 대표적은 분할과 정복 알고리즘을 사용하는 정렬 알고리즘으로 O(NlogN)의 시간 복잡도를 갖는다.
하지만 모든 수가 정렬되어 있을 때 최악의 경우에는 O(N^2)의 시간복잡도를 갖는다.
"""
import random

def quick_sort(data):
    if len(data)<=1:
        return data

    pivot=data[0]

    left=[item for item in data[1:] if item<=pivot]
    right=[item for item in data[1:] if item>pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)

num_list=random.sample(range(100),50)
print(num_list)
num_list=quick_sort(num_list)
print(num_list)