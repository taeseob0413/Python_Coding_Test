"""
트로피 갯수 문제

진열장에 트로피가 전시되어 있고 각각의 높이가 주어진다.
이때 트로피를 왼쪽,오른쪽에서 볼 때의 보이는 트로피의 갯수를 구하는 문제
"""

def tro(data):
    max_num=data[0]
    count=1
    for i in range(1,len(data)):
        if data[i]>max_num:
            count+=1
            max_num=data[i]
    return count

n=int(input())
num_list=[int(input()) for _ in range(n)]

print(tro(num_list))
num_list.reverse()
print(tro(num_list))
