"""
선택 정렬 리뷰

맨 앞부터 기준으로 잡고 그 수를 제외한 오른쪽의 수들 중에서 가장 작은 값을 찾아 바꾸는 정렬 알고리즘
O(N^2)의 시간복잡도를 갖고 수가 전부 정렬이 되어 있는 경우에도 O(N^2)의 시간복잡도를 갖는다.
"""
import random

def selection_sort(data):
    for i in range(len(data)-1):
        min_index=i
        for j in range(i+1,len(data)):
            if data[min_index]>data[j]:
                min_index=j
        data[min_index],data[i]=data[i],data[min_index]

num_list=random.sample(range(100),50)
print(num_list)
selection_sort(num_list)
print(num_list)
