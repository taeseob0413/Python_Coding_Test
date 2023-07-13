"""
모험가 길드 문제

모험가 N 명이 존재할 때 각각의 모험가는 다른 공포도를 갖고 있다.
이때 모험을 떠날 조를 짜는데 공포도가 X인 모험가는 반드시 X명인 조에 속해야 한다.

만들수 있는 최대 그룹의 수를 출력하는 문제

>>이 문제는 전형적인 그리디 알고리즘의 문제이다
>>가장 많은 그룹의 수를 만들기 위해서는 가장 공포도가 낮은 사람들부터 조를 짜는 것이 중요하다.
>>N이 십만이하이므로 O(NlogN)의 시간복잡도를 사용하여 오름차순으로 정렬을 해준뒤 공포도가 낮은 모험가부터 조를 짜주면 된다.
"""
n=int(input())
peple=list(map(int,input().split()))

peple.sort()

count=0
result=0
for i in peple:
    count+=1
    if i<=count:
        result+=1
        count=0

print(result)