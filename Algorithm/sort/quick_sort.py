"""
퀵 정렬

분할과 정복 알고리즘의 예.
기준점(pivot)을 정해서, 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 분류하여 각각의 왼쪽과 오른쪽은 재귀용범을 사용해서 다시 동일 함수를 호출.

시간 복잡도는 O(NlogN)을 따르지만
최악의 경우(pivot이 가장 크거나 가장 작은 원소일 경우)에는 O(N^2)의 시간복잡도를 갖는다.(이미 데이터가 정렬되어 있는 경우)
"""
import random
def quick_sort(data):
    if len(data)<=1:
        return data
    pivot=data[0]
    left=[item for item in data[1:] if item<pivot]
    right=[item for item in data[1:] if item>=pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)

data_list=random.sample(range(100),50)
print(quick_sort(data_list))