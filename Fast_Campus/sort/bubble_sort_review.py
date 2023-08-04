"""
버블 정렬 복습

인접한 두 수를 비교하여 크거나 작을 때 자리를 바꿔주는 알고리즘이다.
시간 복잡도는 O(N^2)을 따르고 모든 수가 정렬되어 있을 때 flag비트를 사용하면 O(N)의 시간복잡도를 갖을 수 있다.
"""
import random

def bubble_sort(data):
    for i in range(len(data)-1):
        flag=False
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                flag=True
        if not flag:
            break

#0~99까지의 숫자중에서 50개를 선택하여 리스트로 반환
num_list=random.sample(range(100),50)

print(num_list)
bubble_sort(num_list)
print(num_list)