"""
만들 수 없는 금액 문제
N개의 동전이 주어질 때 (1<=N<=1000) 주어진 동전으로 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 문제

이 문제의 해결 방법은
targer=1부터 정한 뒤 오름차순 정렬된 동전 리스트의 가장 작은 원소부터 더해나간다.
이때 target=4라고 하는 것은 1,2,3은 이미 만들 수 있는 수 이므로 target보다 동전의 원소가 작기만 하면(ex동전이 3일 경우) 3+1,3+2,3+3이 가능해서
동전의 원소 + target(7) 이 새로운 target이 되는 구조이다.
"""

n=int(input())
coin_list=list(map(int,input().split()))
coin_list.sort()
target=1
for coin in coin_list:
    if target<coin:
        break
    target+=coin

print(target)