"""
모험가 길드 문제
N이 주어지는 데 이는 모험가의 수를 뜻하고  (N<=10만)
다음 줄에 N명의 모험가의 각 공포도가 주어짐.
공포도가 x인 모험가는 x명이상의 그룹에 속해야 함. 이때 N명으로 만들 수 있는 최대 그룹의 수를 구하기.

이 문제는 정렬을 하여서(NlogN) 가장 작은 수의 공포도의 모험가부터 조를 이루는 것이 효과적
ex) 1,1,3 의 공포도의 사람이 존재할 때 1,1,3을 한조로 묶는 방법과 1,1을 각각의 조로 묶고 3을 남겨놓는 방법이 있는데 후자가 많은 그룹이 생김.
"""
n=int(input())
people_list=list(map(int,input().split()))
people_list.sort()
total=0
cur_people=0

for people in people_list:
    cur_people+=1
    if cur_people==people:
        total+=1
        cur_people=0
print(total)