"""
수 정렬하기 문제

>>이 문제의 경우에는 수를 입력받아 정렬한 형태로 출력을 하는 문제.
>>단 데이터의 갯수가 1000만개 이므로 O(NlogN)의 시간복잡도 보다는 계수정렬을 사용하였을 때 좀 더 쉽게 해결할 수 있는 문제.
"""
import sys
input=sys.stdin.readline

n=int(input())
count_list=[0]*(10001)

for _ in range(n):
    count_list[int(input())]+=1

for i in range(10001):
    if count_list[i]!=0:
        for _ in range(count_list[i]):
            print(i)