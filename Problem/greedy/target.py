"""
만들 수 없는 금액 문제
동전 N개가 주어졌을 때 N개의 동전으로 만들 수 없는 최소의 수를 구하는 문제

이 문제의 경우는 target이라는 변수를 설정하는 것이 핵심 문제
target의 의미는 현재까지 주어진 동전으로 1~target-1까지 수를 구현할 수 있다는 데 있음.
"""
n=int(input())
num=list(map(int,input().split()))
num.sort()
target=1
for i in num:
    if target<i:
        break
    else:
        target+=i
print(target)