"""
이 문제의 경우에는 리스트만 사용하여서 풀면 출력 초과가 발생함을 알 수 있다.
heapq를 사용해보기
"""
import heapq

n=int(input())
card=[]
for _ in range(n):
    heapq.heappush(card,int(input()))

sum=0

while len(card)>1:
    a=heapq.heappop(card)
    b=heapq.heappop(card)
    sum+=a+b
    heapq.heappush(card,a+b)

print(sum)