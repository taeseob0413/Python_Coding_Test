"""
삽입 정렬

데이터를 하나씩 확인하면서 각 데이터를 적절한 위치에 삽입하는 정렬 알고리즘.
삽입 정렬은 그 앞까지의 데이터는 모두 정렬되어 있음을 전제로 한다.

O(N^2)의 시간복잡도를 갖고 데이터가 정렬되어 있을 경우에는 O(N)의 시간복잡도를 갖는다.
"""
import random

def insertion_sort(data):
    for i in range(1,len(data)):
        #i번째부터 1번까지만 비교
        for j in range(i,0,-1):
            if data[j]>data[j-1]:
                break
            else:
                data[j],data[j-1]=data[j-1],data[j]

num_list=random.sample(range(100),50)
print(num_list)
insertion_sort(num_list)
print(num_list)