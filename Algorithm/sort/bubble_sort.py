"""
버블 정렬
맨 앞부터 인접한 두 개의 수를 비교하여 앞의 데이터가 뒤의 데이터보다 크다면 자리를 바꾸는 정렬 알고리즘.
시간 복잡도는 O(N^2) 이고 모든 원소가 정렬되어 있을 때 flag비트를 사용하면 O(N)의 시간 복잡도를 갖는다.
"""

#bubble_sort 코드
import random
def bubble_sort(data):
    for i in range(len(data)-1):
        flag = False
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                flag=True
        if not flag:
            break
    return data

#0~99까지의 수에서 50개를 선택하여 리스트로 반환
data_list=random.sample(range(100),50) 
print(bubble_sort(data_list))