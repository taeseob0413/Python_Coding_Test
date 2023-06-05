"""
선택 정렬

주어진 데이터 중, 최소값을 찾아서 데이터 맨 앞에 위치한 값과 교체하고 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 정렬하는 알고리즘.

O(N^2)의 시간복잡도를 갖고 있음 >> 데이터의 개수가 10000개 이상일 경우 성능이 많이 떨어지는 것을 알 수 있음.
데이터가 많은 경우에는 퀵, 병합, 정렬 라이브러리를 사용하는 것이 좋음.

하지만 특정한 리스트에서 가장 작은 데이터를 찾는 일이 코테에서 잦으므로 선택 정렬 소스코드 형태에 익숙해질 필요가 있음.
"""
import random

def selection_sort(data):
    for i in range(len(data)-1):
        min_index=i
        for j in range(i+1,len(data)):
            if data[j]<data[min_index]:
                min_index=j
        data[min_index],data[i]=data[i],data[min_index]
    return data

data_list=random.sample(range(100),50)
print(selection_sort(data_list))