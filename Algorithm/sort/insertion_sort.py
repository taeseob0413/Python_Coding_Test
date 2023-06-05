"""
삽입 정렬

두 번째 인덱스부터 시작하여 해당 인덱스(Key 값) 앞에 있는 데이터부터 비교해서 Key 값이 더 작을 경우 데이터를 뒤 인덱스로 복사하는 과정을
Key값이 더 큰 데이터를 만날때까지 반복하고 바로 뒤에 Key 값을 이동

>>삽입 정렬은 그 앞까지의 데이터는 이미 정렬되어 있다고 가정을 한다.
>>삽입 정렬의 시간복잡도는 O(N^2)이지만 데이터가 거의 정렬되어 있는 경우에는 매우 빠르게 동작하고 최선의 경우 O(N)의 시간복잡도를 갖는다.
"""
import random
def insertion_sort(data):
    for i in range(1,len(data)):
        for j in range(i,0,-1):  #인덱스 i~1까지 감소하며 반복
            if data[j]<data[j-1]:
                data[j],data[j-1]=data[j-1],data[j]
            else:
                break
    return data

data_list=random.sample(range(100),50)
print(insertion_sort(data_list))
