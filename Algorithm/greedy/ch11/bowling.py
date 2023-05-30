"""
볼링공 고르기
A,B 두 사람은 N개의 볼링공이 존재할 때 각각 다른 무게를 선택하려고 함.
같은 무게의 볼링공이 여러개 존재할 수 있지만 각각 다른 공으로 간주한다.
두 사람이 고를 수 있는 볼링공의 조합을 고르기

이 문제의 경우에는 볼링공의 갯수가 최대 1000개 이므로 O(N^2)으로 해도 괜찮음
"""

n,m=map(int,input().split())
bowling_list=list(map(int,input().split()))
count=0
for i in range(len(bowling_list)-1):
    for j in range(i+1,len(bowling_list)):
       if bowling_list[i]!=bowling_list[j]:
           count+=1
print(count)