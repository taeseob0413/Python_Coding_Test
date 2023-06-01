"""
시각 문제
N이 주어졌을 때 0시 00분 00초 ~ N시 59분 59초까지 3을 적어도 한개 포함한 시각을 세는 문제.

이 문제의 경우에도 시간복잡도는 크게 고려하지 않아도 됨,
"""

n=int(input())
count=0
for i in range(n+1):
    if i in [3,13,23]:
       count+=6*10*6*10
    else:
        count+=6*10*6*10-5*9*5*9 #전체에서 3을 적어도 한개이상 포함하지 않는 경우를 빼기

print(count)